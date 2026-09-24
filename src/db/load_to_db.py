"""
Travel Pal — Phase 6: load cleaned data into Postgres.

Run with:
    python -m src.db.load_to_db

Requires Phase 2 to have already produced the cleaned CSVs in
data/processed/, and a running Postgres server with the connection
details set in .env (see src/db/connection.py).
"""

from pathlib import Path

import pandas as pd

from src.db.connection import engine

PROCESSED_DIR = Path(__file__).resolve().parents[2] / "data" / "processed"
DESTINATIONS_FILE = PROCESSED_DIR / "destinations_clean.csv"
ACCOMMODATIONS_FILE = PROCESSED_DIR / "accommodations_clean.csv"


def load_table(csv_path: Path, table_name: str) -> int:
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    return len(df)


def main():
    dest_count = load_table(DESTINATIONS_FILE, "destinations")
    print(f"Loaded {dest_count} rows into 'destinations' table.")

    accom_count = load_table(ACCOMMODATIONS_FILE, "accommodations")
    print(f"Loaded {accom_count} rows into 'accommodations' table.")

    print("Done. Tables 'destinations' and 'accommodations' are ready in Postgres.")


if __name__ == "__main__":
    main()