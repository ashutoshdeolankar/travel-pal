"""
Travel Pal API.

Run locally with:
    uvicorn src.api.main:app --reload
"""

import logging
import time

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from src.models.predict import get_recommendations as predict_recommendations

# ── Logging setup ──────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("travelpal")

app = FastAPI(
    title="Travel Pal API",
    description="Personalized travel, food, and accommodation recommendations.",
    version="0.4.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Request logging middleware ─────────────────────────────
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration_ms = (time.time() - start) * 1000

    logger.info(
        "%s %s → %s (%.0fms)",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )
    return response


# ── Request/Response schemas ───────────────────────────────
class PreferenceRequest(BaseModel):
    budget: str = Field(..., pattern="^(low|mid|high)$", examples=["mid"])
    duration_days: int = Field(..., ge=1, examples=[3])
    interests: list[str] = Field(default_factory=list, examples=[["Temple", "Historical"]])
    top_n: int = Field(default=10, ge=1, le=50)
    category: str = Field(
        default="all",
        pattern="^(all|hidden_gem|well_known)$",
        description="Filter to 'hidden_gem', 'well_known', or 'all' (both).",
    )


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
    category: str
    hidden_gem_score: float
    score: float


class RecommendationResponse(BaseModel):
    recommendations: list[Recommendation]


# ── Endpoints ──────────────────────────────────────────────
@app.get("/health")
def health() -> dict:
    """Basic health check."""
    return {"status": "ok"}


@app.get("/health/detailed")
def health_detailed() -> dict:
    """Detailed health check — verifies database and model status."""
    status = {"api": "ok", "database": "unknown", "model": "unknown"}

    # Check database
    try:
        from sqlalchemy import text
        from src.db.connection import engine
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        status["database"] = "ok"
    except Exception as e:
        status["database"] = f"error: {e}"
        logger.error("Database health check failed: %s", e)

    # Check model
    try:
        from src.models.predict import MODEL_PATH
        if MODEL_PATH.exists():
            status["model"] = "ok"
        else:
            status["model"] = "not found"
    except Exception as e:
        status["model"] = f"error: {e}"
        logger.error("Model health check failed: %s", e)

    overall = "ok" if all(v == "ok" for v in status.values()) else "degraded"
    return {"status": overall, "checks": status}


@app.post("/recommendations", response_model=RecommendationResponse)
def get_recommendations(prefs: PreferenceRequest) -> RecommendationResponse:
    logger.info(
        "Recommendation request: budget=%s, days=%s, interests=%s, top_n=%s, category=%s",
        prefs.budget, prefs.duration_days, prefs.interests, prefs.top_n, prefs.category,
    )
    try:
        results_df = predict_recommendations(
            budget=prefs.budget,
            duration_days=prefs.duration_days,
            interests=prefs.interests,
            top_n=prefs.top_n,
            category=prefs.category,
        )
    except FileNotFoundError as e:
        logger.error("Model not found: %s", e)
        raise HTTPException(
            status_code=503,
            detail=f"Model not trained yet. Run `python -m src.models.train` first. ({e})",
        )
    except Exception as e:
        logger.error("Recommendation failed: %s", e, exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal error: {e}")

    logger.info("Returning %d recommendations", len(results_df))
    recommendations = [Recommendation(**row) for row in results_df.to_dict(orient="records")]
    return RecommendationResponse(recommendations=recommendations)


@app.get("/destinations/{destination_id}")
def get_destination(destination_id: int) -> dict:
    return {"id": destination_id, "name": "TODO: fetch from database"}
