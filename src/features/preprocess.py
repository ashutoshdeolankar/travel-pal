"""
Travel Pal — Phase 2 (v2): cleaning & preprocessing for the combined dataset.

Takes the large raw TravelPal_Combined_India_Dataset.csv (~15k rows) and
produces a clean, deduplicated, model-ready destinations table, plus the
existing accommodations cleaning (unchanged from Phase 1/2).

Key steps, in order:
  1. Keep only rows with rating, category, and city present (drops rows
     too incomplete to be useful).
  2. Drop rows whose category is a business/service, not a destination
     (travel agencies, hotels, government offices, shops, etc.) — see
     EXCLUDE_CATEGORIES.
  3. Deduplicate by (name, city).
  4. Fill missing `state` via a city -> state lookup built from rows
     that do have a state; anything still unresolved is labeled
     "Unknown" rather than dropped.
  5. Derive a `significance` tag (Religious / Historical / Natural /
     Recreational / General) from keywords in the name, category,
     subcategory, tags, and description — because the raw `category`
     field is dominated by an uninformative "Tourist attraction" value
     for most rows.
  6. Estimate `entrance_fee_inr` and `time_needed_hrs` from the derived
     significance, since the source dataset doesn't include these.
     THESE TWO FIELDS ARE ESTIMATES, not scraped values — document this
     in your report/data README.
  7. Tag each destination Hidden Gem / Well-Known using real
     rating + review-count data (this dataset's reviews_count is a
     genuine popularity signal, unlike the old dataset's rounded figure).

Run with:
    python -m src.features.preprocess
"""

from pathlib import Path

import pandas as pd

from src.data.load_data import load_accommodations, load_destinations

PROCESSED_DIR = Path(__file__).resolve().parents[2] / "data" / "processed"

EXCLUDE_CATEGORIES = {
    "travel agency", "tour operator", "tour agency", "sightseeing tour agency",
    "boat tour agency", "bus tour agency", "canoe & kayak tour agency", "scuba tour agency",
    "cruise agency", "car rental agency", "car leasing service", "taxi service",
    "transportation service", "transportation infrastructure", "public transportation system",
    "tourist information center", "tourism development corporation", "state department of tourism",
    "hotel", "resort hotel", "homestay", "indoor lodging", "lodge", "cottage", "villa",
    "dharamshala", "assisted living facility",
    "government office", "local government office", "state government office",
    "municipal administration office", "electricity board", "post office", "office",
    "non-profit organization", "association or organization", "religious organization",
    "news service", "research institute",
    "school", "boarding school", "higher secondary school", "driving school",
    "mountaineering class", "skating instructor",
    "electronics store", "general store", "supermarket", "store", "craft store",
    "souvenir store", "gift shop", "trophy shop", "tailor", "hair salon",
    "photography studio", "plant nursery",
    "coffee shop", "cafe", "restaurant", "seafood restaurant", "modern indian restaurant",
    "caribbean restaurant",
    "movie theater", "movie studio", "casino",
    "airport", "regional airport", "heliport", "harbor", "seaport", "river port",
    "train station", "bus stop", "ferry service", "ferry terminal", "toll booth",
    "water works", "saw mill", "mine",
    "priest", "artist", "event ticket seller", "cremation service", "animal shelter",
    "fishing charter", "dive shop", "rafting", "raft trip outfitter",
}

RELIGIOUS_KEYWORDS = [
    "temple", "mosque", "church", "shrine", "gurudwara", "dargah",
    "monastery", "ashram", "religious", "cathedral", "chapel",
    "basilica", "pilgrimage", "pagoda",
]
HISTORICAL_KEYWORDS = [
    "fort", "palace", "museum", "monument", "landmark", "tomb",
    "mausoleum", "archaeological", "heritage", "memorial", "ruins",
    "historical", "castle", "war memorial", "gate", "haveli", "minar", "qila",
]
NATURAL_KEYWORDS = [
    "park", "garden", "lake", "waterfall", "hill", "nature", "wildlife",
    "sanctuary", "beach", "mountain", "scenic", "forest", "valley",
    "island", "cave", "hiking", "trek", "bird watching", "reserve",
    "falls", "peak", "dam", "river", "ghat",
]
RECREATIONAL_KEYWORDS = [
    "zoo", "amusement", "water park", "adventure", "theme park",
    "aquarium", "golf", "ski", "fountain", "planetarium",
]

ESTIMATED_FEE_BY_SIGNIFICANCE = {
    "Religious": 0, "Historical": 25, "Natural": 20, "Recreational": 100, "General": 0,
}
ESTIMATED_HOURS_BY_SIGNIFICANCE = {
    "Religious": 1.0, "Historical": 1.5, "Natural": 2.0, "Recreational": 2.5, "General": 1.5,
}


def _derive_significance(row) -> str:
    text = " ".join(
        str(x) for x in [
            row.get("name", ""), row.get("category", ""), row.get("subcategory", ""),
            row.get("tags", ""), row.get("description", ""),
        ]
    ).lower()
    if any(k in text for k in RELIGIOUS_KEYWORDS):
        return "Religious"
    if any(k in text for k in HISTORICAL_KEYWORDS):
        return "Historical"
    if any(k in text for k in NATURAL_KEYWORDS):
        return "Natural"
    if any(k in text for k in RECREATIONAL_KEYWORDS):
        return "Recreational"
    return "General"


def clean_destinations(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Only individual attractions — exclude city/town-level summary rows.
    if "record_type" in df.columns:
        df = df[df["record_type"] == "attraction"].copy()

    df = df[df["rating"].notna() & df["category"].notna() & df["city"].notna()].copy()

    df["category_lower"] = df["category"].str.lower().str.strip()
    df = df[~df["category_lower"].isin(EXCLUDE_CATEGORIES)].copy()

    df = df.drop_duplicates(subset=["name", "city"], keep="first")

    known = df[df["state"].notna()]
    city_state_map = known.groupby("city")["state"].agg(lambda x: x.mode()[0])
    df["state"] = df.apply(
        lambda r: r["state"] if pd.notna(r["state"]) else city_state_map.get(r["city"], "Unknown"),
        axis=1,
    )

    df["significance"] = df.apply(_derive_significance, axis=1)

    df["entrance_fee_inr"] = df["significance"].map(ESTIMATED_FEE_BY_SIGNIFICANCE)
    df["time_needed_hrs"] = df["significance"].map(ESTIMATED_HOURS_BY_SIGNIFICANCE)

    df["type"] = df["subcategory"].fillna(df["category"])
    df["best_time_to_visit"] = df["best_time"].fillna("Anytime")
    df = df.rename(columns={"rating": "avg_rating", "reviews_count": "num_reviews"})
    df["num_reviews"] = df["num_reviews"].fillna(0)

    # Carry forward any human-assigned hidden_gem label (only present for
    # a small curated subset) so we can check our automated scoring
    # against it as a sanity check, without relying on it for coverage.
    if "hidden_gem" in df.columns:
        df["human_label"] = df["hidden_gem"]
    else:
        df["human_label"] = None

    if "destination_id" in df.columns:
        df = df.drop(columns=["destination_id"])
    df = df.reset_index(drop=True)
    df.insert(0, "destination_id", range(1, len(df) + 1))

    return df[[
        "destination_id", "name", "city", "state", "type", "significance",
        "avg_rating", "num_reviews", "entrance_fee_inr", "time_needed_hrs",
        "best_time_to_visit", "latitude", "longitude", "human_label",
    ]]


def tag_hidden_gems(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    rating_median = df["avg_rating"].median()
    reviews_median = df["num_reviews"].median()

    rating_range = df["avg_rating"].max() - df["avg_rating"].min()
    reviews_range = df["num_reviews"].max() - df["num_reviews"].min()

    rating_norm = (
        (df["avg_rating"] - df["avg_rating"].min()) / rating_range if rating_range > 0 else 0.5
    )
    popularity_norm = (
        (df["num_reviews"] - df["num_reviews"].min()) / reviews_range if reviews_range > 0 else 0.5
    )
    df["hidden_gem_score"] = (rating_norm * (1 - popularity_norm)).round(3)

    df["category"] = "Well-Known"
    is_hidden_gem = (df["avg_rating"] >= rating_median) & (df["num_reviews"] < reviews_median)
    df.loc[is_hidden_gem, "category"] = "Hidden Gem"

    # Validate against any human-labeled subset, where present.
    labeled = df[df["human_label"].notna()]
    if len(labeled) > 0:
        human_as_category = labeled["human_label"].replace({"Famous": "Well-Known"})
        agree = (human_as_category == labeled["category"]).sum()
        print(
            f"Validation: {len(labeled)} destinations had a human-assigned "
            f"Famous/Hidden Gem label. Our automated scoring agreed with "
            f"{agree}/{len(labeled)} ({agree/len(labeled):.0%}) of them."
        )

    return df


def clean_accommodations(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["has_rating"] = df["stars"].notna()
    median_rating = df["stars"].median()
    df["stars"] = df["stars"].fillna(median_rating)
    df = df.rename(
        columns={
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


def match_city_from_address(address, known_cities):
    if not isinstance(address, str):
        return None
    address_lower = address.lower()
    for city in known_cities:
        if isinstance(city, str) and city.lower() in address_lower:
            return city
    return None


def link_accommodations_to_destinations(destinations, accommodations):
    accommodations = accommodations.copy()
    known_cities = sorted(destinations["city"].dropna().unique().tolist())
    accommodations["matched_city"] = accommodations["address"].apply(
        lambda addr: match_city_from_address(addr, known_cities)
    )
    matched = accommodations["matched_city"].notna().sum()
    total = len(accommodations)
    print(f"Matched {matched}/{total} accommodation listings to a known destination city ({matched/total:.0%}).")
    return accommodations


def main():
    raw_destinations = load_destinations()
    raw_accommodations = load_accommodations()

    destinations = clean_destinations(raw_destinations)
    destinations = tag_hidden_gems(destinations)

    accommodations = clean_accommodations(raw_accommodations)
    accommodations = link_accommodations_to_destinations(destinations, accommodations)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    destinations.to_csv(PROCESSED_DIR / "destinations_clean.csv", index=False)
    accommodations.to_csv(PROCESSED_DIR / "accommodations_clean.csv", index=False)

    print(f"\nSaved {len(destinations)} cleaned destinations.")
    print("Significance distribution:")
    print(destinations["significance"].value_counts().to_string())
    print("\nHidden Gem / Well-Known split:")
    print(destinations["category"].value_counts().to_string())
    print(f"\nSaved {len(accommodations)} cleaned accommodations.")


if __name__ == "__main__":
    main()
