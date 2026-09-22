"""
Travel Pal API — Phase 0 stub.

Run locally with:
    uvicorn src.api.main:app --reload

This is intentionally minimal right now: /recommendations returns
placeholder data. Wire it up to src/models/predict.py once Phase 3
(the model) exists.
"""

from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Travel Pal API",
    description="Personalized travel, food, and accommodation recommendations.",
    version="0.1.0",
)


class PreferenceRequest(BaseModel):
    budget: str = Field(..., examples=["budget", "mid", "luxury"])
    duration_days: int = Field(..., ge=1, examples=[5])
    interests: List[str] = Field(default_factory=list, examples=[["beach", "food"]])


class Recommendation(BaseModel):
    id: str
    name: str
    type: str
    score: float


class RecommendationResponse(BaseModel):
    recommendations: List[Recommendation]


@app.get("/health")
def health() -> dict:
    """Used by monitoring/load balancers to check the service is alive."""
    return {"status": "ok"}


@app.post("/recommendations", response_model=RecommendationResponse)
def get_recommendations(prefs: PreferenceRequest) -> RecommendationResponse:
    """
    Placeholder implementation.

    TODO (Phase 3/5): replace this with a real call into
    src/models/predict.py, which loads the trained model
    (from the MLflow registry or a saved artifact) and scores
    destinations against `prefs`.
    """
    dummy_results = [
        Recommendation(id="dest_001", name="Placeholder Destination A", type="destination", score=0.92),
        Recommendation(id="dest_002", name="Placeholder Destination B", type="destination", score=0.85),
    ]
    return RecommendationResponse(recommendations=dummy_results)


@app.get("/destinations/{destination_id}")
def get_destination(destination_id: str) -> dict:
    """Placeholder — wire up to the database in Phase 6."""
    return {"id": destination_id, "name": "TODO: fetch from database"}
