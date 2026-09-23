"""
Travel Pal — Phase 3: inference.

Loads the trained model artifact and scores destinations against a
user's stated preferences. This is what the API (Phase 5) calls.

Quick manual test:
    python -m src.models.predict
"""

from pathlib import Path
from typing import List

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

MODEL_PATH = Path(__file__).resolve().parents[2] / "data" / "processed" / "model" / "recommender.joblib"
DESTINATIONS_FILE = Path(__file__).resolve().parents[2] / "data" / "processed" / "destinations_clean.csv"

_model_cache = None
_destinations_cache = None


def _load_artifacts():
    """Loads once per process and caches — avoids re-reading disk on every API request."""
    global _model_cache, _destinations_cache
    if _model_cache is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"{MODEL_PATH} not found. Run `python -m src.models.train` first."
            )
        _model_cache = joblib.load(MODEL_PATH)
        _destinations_cache = pd.read_csv(DESTINATIONS_FILE)
    return _model_cache, _destinations_cache


def _build_user_vector(interests: List[str], model: dict) -> np.ndarray:
    """
    Builds a feature vector for the user in the same space as the
    destination feature matrix: 1.0 for each requested type/significance
    tag that matches a known category, 0 elsewhere for categoricals.
    Numeric columns (avg_rating, num_reviews_lakhs) are set to the
    dataset mean (0 after scaling) — i.e. "no preference", since the
    user isn't expressing a rating preference, they're expressing topic
    interests.
    """
    encoder = model["encoder"]
    categorical_cols = model["categorical_cols"]
    numeric_cols = model["numeric_cols"]

    interests_lower = {tag.lower() for tag in interests}

    cat_vector_parts = []
    for col_idx, categories in enumerate(encoder.categories_):
        col_vector = np.array(
            [1.0 if str(cat).lower() in interests_lower else 0.0 for cat in categories]
        )
        cat_vector_parts.append(col_vector)
    cat_vector = np.concatenate(cat_vector_parts) if cat_vector_parts else np.array([])

    # neutral (mean = 0 after scaling) numeric preference
    num_vector = np.zeros(len(numeric_cols))

    return np.concatenate([cat_vector, num_vector]).reshape(1, -1)


def _apply_budget_duration_filter(
    df: pd.DataFrame, budget: str, duration_days: int, budget_thresholds: dict
) -> pd.DataFrame:
    """
    budget: "low" | "mid" | "high"
    Filters by entrance fee tier and by whether the destination's
    time-needed fits inside a reasonable per-day sightseeing budget
    (assumes ~8 active hours/day, leaves room for multiple stops).
    """
    df = df.copy()
    low_cutoff = budget_thresholds["low_cutoff"]
    mid_cutoff = budget_thresholds["mid_cutoff"]

    if budget == "low":
        df = df[df["entrance_fee_inr"] <= low_cutoff]
    elif budget == "mid":
        df = df[df["entrance_fee_inr"] <= mid_cutoff]
    # "high" — no fee filter, everything is in budget

    max_hours = duration_days * 8
    df = df[df["time_needed_hrs"] <= max_hours]

    return df


def get_recommendations(
    budget: str, duration_days: int, interests: List[str], top_n: int = 10
) -> pd.DataFrame:
    """
    Main entrypoint. Returns a DataFrame of the top_n recommended
    destinations with a similarity `score` column, sorted descending.
    """
    model, destinations = _load_artifacts()

    filtered = _apply_budget_duration_filter(
        destinations, budget, duration_days, model["budget_thresholds"]
    )
    if filtered.empty:
        # fall back to unfiltered rather than returning nothing —
        # better to show something than an empty result for a demo
        filtered = destinations.copy()

    filtered_positions = filtered.index.to_numpy()
    filtered_feature_matrix = model["feature_matrix"][filtered_positions]

    user_vector = _build_user_vector(interests, model)
    similarities = cosine_similarity(user_vector, filtered_feature_matrix)[0]

    result = filtered.copy()
    result["score"] = similarities
    result = result.sort_values("score", ascending=False).head(top_n)
    return result[
        [
            "destination_id",
            "name",
            "city",
            "state",
            "type",
            "significance",
            "avg_rating",
            "entrance_fee_inr",
            "time_needed_hrs",
            "score",
        ]
    ]


if __name__ == "__main__":
    # Quick manual sanity check
    results = get_recommendations(
        budget="mid", duration_days=3, interests=["Temple", "Historical"], top_n=5
    )
    print(results.to_string(index=False))