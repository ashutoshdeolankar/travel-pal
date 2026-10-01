"""
Travel Pal — Phase 3/6: inference.

Loads the trained model artifact and scores destinations against a
user's stated preferences. This is what the API (Phase 5) calls.

Destination metadata (name, city, rating, hidden-gem category, etc.)
is read from Postgres. The trained similarity model itself still comes
from the joblib file produced by train.py. Destinations are fetched
ordered by destination_id so row order lines up with training order.

Quick manual test:
    python -m src.models.predict
"""

from pathlib import Path
from typing import List

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from src.db.connection import engine

MODEL_PATH = Path(__file__).resolve().parents[2] / "data" / "processed" / "model" / "recommender.joblib"

_model_cache = None
_destinations_cache = None


def _load_artifacts():
    global _model_cache, _destinations_cache
    if _model_cache is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"{MODEL_PATH} not found. Run `python -m src.models.train` first."
            )
        _model_cache = joblib.load(MODEL_PATH)
        _destinations_cache = pd.read_sql(
            "SELECT * FROM destinations ORDER BY destination_id", engine
        )
    return _model_cache, _destinations_cache


def _build_user_vector(interests: List[str], model: dict) -> np.ndarray:
    encoder = model["encoder"]
    numeric_cols = model["numeric_cols"]

    interests_lower = {tag.lower() for tag in interests}

    cat_vector_parts = []
    for categories in encoder.categories_:
        col_vector = np.array(
            [1.0 if str(cat).lower() in interests_lower else 0.0 for cat in categories]
        )
        cat_vector_parts.append(col_vector)
    cat_vector = np.concatenate(cat_vector_parts) if cat_vector_parts else np.array([])

    num_vector = np.zeros(len(numeric_cols))

    return np.concatenate([cat_vector, num_vector]).reshape(1, -1)


def _apply_budget_duration_filter(df, budget, duration_days, budget_thresholds):
    df = df.copy()
    low_cutoff = budget_thresholds["low_cutoff"]
    mid_cutoff = budget_thresholds["mid_cutoff"]

    if budget == "low":
        df = df[df["entrance_fee_inr"] <= low_cutoff]
    elif budget == "mid":
        df = df[df["entrance_fee_inr"] <= mid_cutoff]

    max_hours = duration_days * 8
    df = df[df["time_needed_hrs"] <= max_hours]

    return df


def get_recommendations(
    budget: str,
    duration_days: int,
    interests: List[str],
    top_n: int = 10,
    category: str = "all",
) -> pd.DataFrame:
    """
    category: "all" | "hidden_gem" | "well_known" — filters results to
    only Hidden Gem or only Well-Known places, or leaves both in ("all").
    """
    model, destinations = _load_artifacts()

    filtered = _apply_budget_duration_filter(
        destinations, budget, duration_days, model["budget_thresholds"]
    )
    if filtered.empty:
        filtered = destinations.copy()

    if category == "hidden_gem":
        filtered = filtered[filtered["category"] == "Hidden Gem"]
    elif category == "well_known":
        filtered = filtered[filtered["category"] == "Well-Known"]
    if filtered.empty:
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
            "category",
            "hidden_gem_score",
            "score",
        ]
    ]


if __name__ == "__main__":
    results = get_recommendations(
        budget="mid", duration_days=3, interests=["Temple", "Historical"], top_n=5
    )
    print(results.to_string(index=False))
