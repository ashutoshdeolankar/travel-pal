"""
Travel Pal — Phase 3/4 (v2): train the content-based recommendation model.
Updated for the larger combined dataset — numeric feature renamed from
num_reviews_lakhs to num_reviews (a real review count now, not a proxy).
"""

from pathlib import Path

import joblib
import mlflow
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder, StandardScaler

PROCESSED_DIR = Path(__file__).resolve().parents[2] / "data" / "processed"
MODEL_DIR = PROCESSED_DIR / "model"
DESTINATIONS_FILE = PROCESSED_DIR / "destinations_clean.csv"

CATEGORICAL_COLS = ["type", "significance"]
NUMERIC_COLS = ["avg_rating", "num_reviews"]


def load_clean_destinations() -> pd.DataFrame:
    if not DESTINATIONS_FILE.exists():
        raise FileNotFoundError(f"{DESTINATIONS_FILE} not found. Run preprocess first.")
    return pd.read_csv(DESTINATIONS_FILE)


def build_feature_matrix(df: pd.DataFrame):
    encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    cat_features = encoder.fit_transform(df[CATEGORICAL_COLS])
    scaler = StandardScaler()
    num_features = scaler.fit_transform(df[NUMERIC_COLS])
    feature_matrix = np.hstack([cat_features, num_features])
    return feature_matrix, encoder, scaler


def compute_budget_thresholds(df: pd.DataFrame) -> dict:
    low_cutoff = df["entrance_fee_inr"].quantile(0.33)
    mid_cutoff = df["entrance_fee_inr"].quantile(0.66)
    return {"low_cutoff": float(low_cutoff), "mid_cutoff": float(mid_cutoff)}


def evaluate(feature_matrix: np.ndarray) -> float:
    sims = cosine_similarity(feature_matrix)
    n = sims.shape[0]
    off_diagonal_sum = sims.sum() - np.trace(sims)
    return float(off_diagonal_sum / (n * (n - 1)))


def main():
    df = load_clean_destinations()
    feature_matrix, encoder, scaler = build_feature_matrix(df)
    budget_thresholds = compute_budget_thresholds(df)
    avg_pairwise_similarity = evaluate(feature_matrix)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    artifact = {
        "feature_matrix": feature_matrix,
        "encoder": encoder,
        "scaler": scaler,
        "destination_ids": df["destination_id"].tolist(),
        "budget_thresholds": budget_thresholds,
        "categorical_cols": CATEGORICAL_COLS,
        "numeric_cols": NUMERIC_COLS,
    }
    model_path = MODEL_DIR / "recommender.joblib"
    joblib.dump(artifact, model_path)

    mlflow.set_experiment("travel-pal-recommender")
    with mlflow.start_run():
        mlflow.log_param("similarity_metric", "cosine")
        mlflow.log_param("categorical_cols", CATEGORICAL_COLS)
        mlflow.log_param("numeric_cols", NUMERIC_COLS)
        mlflow.log_param("num_destinations", len(df))
        mlflow.log_metric("avg_pairwise_similarity", avg_pairwise_similarity)
        mlflow.log_metric("low_budget_cutoff_inr", budget_thresholds["low_cutoff"])
        mlflow.log_metric("mid_budget_cutoff_inr", budget_thresholds["mid_cutoff"])
        mlflow.log_artifact(str(model_path))

    print(f"Trained on {len(df)} destinations.")
    print(f"Feature vector size: {feature_matrix.shape[1]}")
    print(f"Avg pairwise similarity: {avg_pairwise_similarity:.4f}")
    print(f"Budget thresholds (INR): {budget_thresholds}")
    print(f"Model saved to: {model_path}")


if __name__ == "__main__":
    main()
