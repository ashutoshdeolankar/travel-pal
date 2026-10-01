"""
Travel Pal — Phase 1 (v2): data loading.

Destinations now come from TravelPal_Combined_India_Dataset.csv — a
much larger real dataset (~15k rows scraped from Google Maps listings)
covering places, ratings, real review counts, categories, tags, and
descriptions across India. Place it at:

    data/raw/travelpal_combined_india.csv

Accommodations still come from the original Kaggle Airbnb-style
dataset (unchanged from Phase 1):

    data/raw/india_airbnb_listings.csv

Run this module with:
    python -m src.data.load_data
"""

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"

DESTINATIONS_FILE = RAW_DIR / "travelpal_india_combined_v2.csv"
LISTINGS_FILE = RAW_DIR / "india_airbnb_listings.csv"


def load_destinations() -> pd.DataFrame:
    """
    Load the raw combined destinations CSV. Expected columns include:
    destination_id, name, city, state, country, category, subcategory,
    rating, reviews_count, description, tags, best_time, latitude,
    longitude, address, and a few others. Cleaning/filtering happens in
    src/features/preprocess.py, not here — this just loads the raw file.
    """
    if not DESTINATIONS_FILE.exists():
        raise FileNotFoundError(
            f"{DESTINATIONS_FILE} not found. Place the combined dataset CSV there."
        )
    df = pd.read_csv(DESTINATIONS_FILE)
    print(f"Loaded {len(df)} raw destination rows with columns: {list(df.columns)}")
    return df


def load_accommodations() -> pd.DataFrame:
    if not LISTINGS_FILE.exists():
        raise FileNotFoundError(
            f"{LISTINGS_FILE} not found. Download the accommodations "
            "dataset from Kaggle and place it there (unchanged from Phase 1)."
        )
    df = pd.read_csv(LISTINGS_FILE)
    print(f"Loaded {len(df)} accommodation listings with columns: {list(df.columns)}")
    return df


def basic_sanity_check(df: pd.DataFrame, name: str) -> None:
    print(f"\n--- {name} ---")
    print("shape:", df.shape)
    print("null counts:\n", df.isnull().sum())


def main():
    destinations = load_destinations()
    accommodations = load_accommodations()
    basic_sanity_check(destinations, "destinations (raw)")
    basic_sanity_check(accommodations, "accommodations")


if __name__ == "__main__":
    main()
