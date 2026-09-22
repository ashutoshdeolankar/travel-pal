"""
Travel Pal — Phase 1: data loading.

Before running this, download the two datasets from Kaggle and place
the raw CSVs here:

    data/raw/india_destinations.csv
        <- from "Travel Dataset: Guide to India's Must See Places"
           https://www.kaggle.com/datasets/saketk511/travel-dataset-guide-to-indias-must-see-places

    data/raw/india_airbnb_listings.csv
        <- from "India's Airbnb Gems 2024: Trending Picks"
           https://www.kaggle.com/datasets/kanchana1990/indias-airbnb-gems-2024-trending-picks

Easiest way to get them (once you've set up a free Kaggle account +
API token, see https://www.kaggle.com/docs/api):

    kaggle datasets download -d saketk511/travel-dataset-guide-to-indias-must-see-places -p data/raw --unzip
    kaggle datasets download -d kanchana1990/indias-airbnb-gems-2024-trending-picks -p data/raw --unzip

Then rename the downloaded CSVs to match the filenames above (or
adjust the paths below).

Run this module with:
    python -m src.data.load_data
"""

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"

DESTINATIONS_FILE = RAW_DIR / "india_destinations.csv"
LISTINGS_FILE = RAW_DIR / "india_airbnb_listings.csv"


def load_destinations() -> pd.DataFrame:
    """
    Load the raw destinations CSV.

    Expected columns (from the Kaggle dataset): Zone, State, City, Name,
    Type, Establishment Year, time needed to visit in hrs,
    Google review rating, Entrance Fee in INR, Airport with 50km Radius,
    Weekly Off, Significance, DSLR Allowed, Number of google review in
    lakhs, Best Time to visit.
    """
    if not DESTINATIONS_FILE.exists():
        raise FileNotFoundError(
            f"{DESTINATIONS_FILE} not found. Download the destinations "
            "dataset from Kaggle and place it there — see the module "
            "docstring for the exact link and filename."
        )
    df = pd.read_csv(DESTINATIONS_FILE)
    print(f"Loaded {len(df)} destinations with columns: {list(df.columns)}")
    return df


def load_accommodations() -> pd.DataFrame:
    """
    Load the raw Airbnb-style accommodations CSV.

    Expected columns (from the Kaggle dataset): address,
    isHostedBySuperhost, location/lat, location/lng, name,
    numberOfGuests, pricing/rate/amount, roomType, stars.
    """
    if not LISTINGS_FILE.exists():
        raise FileNotFoundError(
            f"{LISTINGS_FILE} not found. Download the accommodations "
            "dataset from Kaggle and place it there — see the module "
            "docstring for the exact link and filename."
        )
    df = pd.read_csv(LISTINGS_FILE)
    print(f"Loaded {len(df)} accommodation listings with columns: {list(df.columns)}")
    return df


def basic_sanity_check(df: pd.DataFrame, name: str) -> None:
    """Quick print-out of shape, nulls, and dtypes — run this before any cleaning."""
    print(f"\n--- {name} ---")
    print("shape:", df.shape)
    print("null counts:\n", df.isnull().sum())
    print("dtypes:\n", df.dtypes)


def main():
    destinations = load_destinations()
    accommodations = load_accommodations()

    basic_sanity_check(destinations, "destinations")
    basic_sanity_check(accommodations, "accommodations")


if __name__ == "__main__":
    main()
