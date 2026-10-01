"""Upsert destinations_clean.csv and cities_clean.csv into PostgreSQL (safe to re-run)."""
import sys
import pandas as pd
from sqlalchemy import create_engine, text

DB_URL = sys.argv[1] if len(sys.argv) > 1 else "postgresql://user:password@localhost:5432/travelpal"
DATA = sys.argv[2] if len(sys.argv) > 2 else "data/processed"

engine = create_engine(DB_URL)


def upsert(df, table, key="id"):
    """Load into a staging table, then INSERT ... ON CONFLICT (id) DO UPDATE."""
    cols = list(df.columns)
    with engine.begin() as con:
        df.to_sql(f"{table}_staging", con, if_exists="replace", index=False)
        exists = con.execute(text("SELECT to_regclass(:t)"), {"t": table}).scalar()
        if not exists:
            con.execute(text(f"CREATE TABLE {table} AS SELECT * FROM {table}_staging WHERE false"))
            con.execute(text(f"ALTER TABLE {table} ADD PRIMARY KEY ({key})"))
        col_list = ", ".join(f'"{c}"' for c in cols)
        updates = ", ".join(f'"{c}" = EXCLUDED."{c}"' for c in cols if c != key)
        con.execute(text(
            f'INSERT INTO {table} ({col_list}) SELECT {col_list} FROM {table}_staging '
            f'ON CONFLICT ({key}) DO UPDATE SET {updates}'))
        con.execute(text(f"DROP TABLE {table}_staging"))
        n = con.execute(text(f"SELECT count(*) FROM {table}")).scalar()
    print(f"{table}: {n} rows")


upsert(pd.read_csv(f"{DATA}/destinations_clean.csv"), "destinations")
upsert(pd.read_csv(f"{DATA}/cities_clean.csv"), "cities")
