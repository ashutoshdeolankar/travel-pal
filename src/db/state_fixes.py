"""Fix places whose state was saved as 'Unknown' in the cleaned data."""

import pandas as pd

# Only cities that are clearly inside one state.
CITY_TO_STATE = {
    "Bijbehara": "Jammu and Kashmir",
    "Gulmarg": "Jammu and Kashmir",
    "Jammu": "Jammu and Kashmir",
    "Vaishno": "Jammu and Kashmir",
    "Amarnath": "Jammu and Kashmir",
    "Leh": "Ladakh",
    "Doimukh": "Arunachal Pradesh",
    "Melongkang Village": "Nagaland",
}


def fix_unknown_states(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy where known cities no longer have state 'Unknown'."""
    df = df.copy()
    unknown = df["state"] == "Unknown"
    fixed = df.loc[unknown, "city"].map(CITY_TO_STATE)
    df.loc[unknown, "state"] = fixed.fillna("Unknown")
    return df

# Cities in the data that are not in India (Spain and Mexico).
NON_INDIA_CITIES = {"Jerez", "Delicias"}


def drop_non_india_places(df: pd.DataFrame) -> pd.DataFrame:
    """Remove places outside India and renumber the rows."""
    outside = (df["state"] == "Unknown") & df["city"].isin(NON_INDIA_CITIES)
    return df[~outside].reset_index(drop=True)


def clean_locations(df: pd.DataFrame) -> pd.DataFrame:
    """Fix known states, then drop places outside India."""
    return drop_non_india_places(fix_unknown_states(df))