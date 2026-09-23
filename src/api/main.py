"""
Travel Pal API.

Run locally with:
    uvicorn src.api.main:app --reload

/recommendations now calls the real trained model (src/models/predict.py).
Run `python -m src.models.train` at least once before starting the API,
or this will raise FileNotFoundError on the first request.
"""

from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.models.predict import get_recommendations as predict_recommendations

app = FastAPI(
    title="Travel Pal API",
    description="Personalized travel, food, and accommodation recommendations.",
    version="0.2.0",
)


class PreferenceRequest(BaseModel):
    budget: str = Field(..., pattern="^(low|mid|high)$", examples=["mid"])
    duration_days: int = Field(..., ge=1, examples=[3])
    interests: List[str] = Field(
        default_factory=list, examples=[["Temple", "Historical"]]
    )
    top_n: int = Field(default=10, ge=1, le=50)


class Recommendation(BaseModel):
    destination_id: int
    name: str
    city: str
    state: str
    type: str
    significance: str
    avg_rating: float
    entrance_fee_inr: float
    time_needed_hrs: float
    score: float


class RecommendationResponse(BaseModel):
    recommendations: List[Recommendation]


@app.get("/health")
def health() -> dict:
    """Used by monitoring/load balancers to check the service is alive."""
    return {"status": "ok"}


@app.post("/recommendations", response_model=RecommendationResponse)
def get_recommendations(prefs: PreferenceRequest) -> RecommendationResponse:
    try:
        results_df = predict_recommendations(
            budget=prefs.budget,
            duration_days=prefs.duration_days,
            interests=prefs.interests,
            top_n=prefs.top_n,
        )
    except FileNotFoundError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Model not trained yet. Run `python -m src.models.train` first. ({e})",
        )

    recommendations = [
        Recommendation(**row) for row in results_df.to_dict(orient="records")
    ]
    return RecommendationResponse(recommendations=recommendations)


@app.get("/destinations/{destination_id}")
def get_destination(destination_id: int) -> dict:
    """Placeholder — wire up to the database in Phase 6."""
    return {"id": destination_id, "name": "TODO: fetch from database"}