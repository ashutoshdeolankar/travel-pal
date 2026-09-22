"""
Travel Pal — model training entrypoint (Phase 3/4 stub).

Run with:
    python -m src.models.train

Fill in once Phase 2 (processed data) exists. The shape below is a
starting point for a content-based recommender using scikit-learn,
with MLflow logging wired in so tracking is a habit from the first
real run, not something bolted on later.
"""

import mlflow
import mlflow.sklearn
# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder, StandardScaler
# from sklearn.metrics.pairwise import cosine_similarity


def load_processed_data():
    """TODO: load from data/processed/ once Phase 2 produces it."""
    raise NotImplementedError("Wire this up once Phase 2 (preprocessing) is done.")


def build_and_train():
    """TODO: build the content-based similarity model."""
    raise NotImplementedError("Wire this up in Phase 3.")


def main():
    mlflow.set_experiment("travel-pal-recommender")
    with mlflow.start_run():
        # Example of the logging pattern to use once training is implemented:
        # mlflow.log_param("similarity_metric", "cosine")
        # mlflow.log_metric("precision_at_k", precision_score)
        # mlflow.sklearn.log_model(model, "model")
        print("TODO: implement load_processed_data() and build_and_train(),")
        print("then log params/metrics/model here before removing this stub.")


if __name__ == "__main__":
    main()
