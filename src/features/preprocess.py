"""
Travel Pal — Phase 2: cleaning & preprocessing.

Takes the raw dataframes from src/data/load_data.py and produces clean,
model-ready dataframes, saved to data/processed/.

Run with:
    python -m src.features.preprocess
"""

from pathlib import Path

import pandas as pd

from src.data.load_data import load_accommodations, load_destinations

PROCESSED_DIR = Path(__file__).resolve().parents[2] / "data" / "processed"


def clean_destinations(df: pd.DataFrame) -> pd.DataFrame:
    """
    - Drops the leftover index column from the CSV export.
    - Standardizes City for joining later.
    - Fills the (mostly legitimate) missing 'Weekly Off' with 'None'
      rather than dropping those rows — 90% of destinations don't have
      a weekly closure day, that's real information, not missing data.
    """
    df = df.copy()

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    df["City"] = df["City"].astype(str).str.strip().str.title()
    df["Weekly Off"] = df["Weekly Off"].fillna("None")

    df = df.rename(
        columns={
            "Name": "name",
            "Type": "type",
            "Zone": "zone",
            "State": "state",
            "City": "city",
            "Establishment Year": "establishment_year",
            "time needed to visit in hrs": "time_needed_hrs",
            "Google review rating": "avg_rating",
            "Entrance Fee in INR": "entrance_fee_inr",
            "Airport with 50km Radius": "airport_within_50km",
            "Weekly Off": "weekly_off",
            "Significance": "significance",
            "DSLR Allowed": "dslr_allowed",
            "Number of google review in lakhs": "num_reviews_lakhs",
            "Best Time to visit": "best_time_to_visit",
        }
    )
    df.insert(0, "destination_id", range(1, len(df) + 1))
    return df


def clean_accommodations(df: pd.DataFrame) -> pd.DataFrame:
    """
    - Adds `has_rating` so the model can distinguish "genuinely unrated"
      from "rated low" instead of the two looking the same after fillna.
    - Fills missing `stars` with the dataset's own median rather than 0,
      so unrated listings don't look artificially terrible to the model.
    - Extracts a best-guess city from the free-text `address` field.
    """
    df = df.copy()

    df["has_rating"] = df["stars"].notna()
    median_rating = df["stars"].median()
    df["stars"] = df["stars"].fillna(median_rating)

    df = df.rename(
        columns={
            "name": "name",
            "address": "address",
            "isHostedBySuperhost": "is_superhost",
            "location/lat": "lat",
            "location/lng": "lon",
            "numberOfGuests": "num_guests",
            "pricing/rate/amount": "price_per_night",
            "roomType": "room_type",
            "stars": "avg_rating",
        }
    )
    df.insert(0, "listing_id", range(1, len(df) + 1))
    return df


def match_city_from_address(address: str, known_cities: list[str]) -> str | None:
    """
    Best-effort match: returns the first known destination city that
    appears as a substring of the listing's address, case-insensitive.
    Returns None if no known city name appears in the address at all —
    those rows stay unmatched rather than being guessed incorrectly.
    """
    if not isinstance(address, str):
        return None
    address_lower = address.lower()
    for city in known_cities:
        if city.lower() in address_lower:
            return city
    return None


def link_accommodations_to_destinations(
    destinations: pd.DataFrame, accommodations: pd.DataFrame
) -> pd.DataFrame:
    """
    Adds a `matched_city` column to accommodations by searching each
    listing's address for a known destination city name.

    This is a simple heuristic, not a guaranteed-correct join — print
    the match rate after running this and sanity-check a sample before
    trusting it for anything beyond a v1 demo.
    """
    accommodations = accommodations.copy()
    known_cities = sorted(destinations["city"].unique().tolist())
    accommodations["matched_city"] = accommodations["address"].apply(
        lambda addr: match_city_from_address(addr, known_cities)
    )
    matched = accommodations["matched_city"].notna().sum()
    total = len(accommodations)
    print(
        f"Matched {matched}/{total} accommodation listings to a known "
        f"destination city ({matched / total:.0%})."
    )
    return accommodations


def main():
    raw_destinations = load_destinations()
    raw_accommodations = load_accommodations()

    destinations = clean_destinations(raw_destinations)
    accommodations = clean_accommodations(raw_accommodations)
    accommodations = link_accommodations_to_destinations(destinations, accommodations)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    destinations.to_csv(PROCESSED_DIR / "destinations_clean.csv", index=False)
    accommodations.to_csv(PROCESSED_DIR / "accommodations_clean.csv", index=False)

    print(f"\nSaved {len(destinations)} cleaned destinations to "
          f"{PROCESSED_DIR / 'destinations_clean.csv'}")
    print(f"Saved {len(accommodations)} cleaned accommodations to "
          f"{PROCESSED_DIR / 'accommodations_clean.csv'}")


if __name__ == "__main__":
    main()