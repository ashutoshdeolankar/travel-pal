import joblib
import pandas as pd

from src.db.connection import engine
from src.models.predict import MODEL_PATH


def test_model_and_database_have_the_same_places_in_the_same_order():
    model = joblib.load(MODEL_PATH)
    ids = pd.read_sql(
        "SELECT destination_id FROM destinations ORDER BY destination_id", engine
    )["destination_id"].tolist()

    assert model["feature_matrix"].shape[0] == len(ids)
    assert model["destination_ids"] == ids