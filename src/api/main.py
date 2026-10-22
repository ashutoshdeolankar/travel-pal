"""
Vishwaara API.

Run locally with:
    uvicorn src.api.main:app --reload
"""

import hashlib
import json
import logging
import time
from collections import defaultdict

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
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
    title="Vishwaara API",
    description="Personalized travel, food, and accommodation recommendations.",
    version="0.5.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Rate Limiting (in-memory) ──────────────────────────────
# Max 30 requests per minute per IP address
RATE_LIMIT = 30
RATE_WINDOW_SECONDS = 60
_rate_tracker: dict[str, list[float]] = defaultdict(list)


def _is_rate_limited(client_ip: str) -> bool:
    """Check if a client IP has exceeded the rate limit."""
    now = time.time()
    # Remove old timestamps outside the window
    _rate_tracker[client_ip] = [
        t for t in _rate_tracker[client_ip]
        if now - t < RATE_WINDOW_SECONDS
    ]
    if len(_rate_tracker[client_ip]) >= RATE_LIMIT:
        return True
    _rate_tracker[client_ip].append(now)
    return False


# ── Response Cache (in-memory, 5-minute TTL) ───────────────
CACHE_TTL_SECONDS = 300  # 5 minutes
_cache: dict[str, tuple[float, dict]] = {}


def _get_cache_key(prefs: dict) -> str:
    """Create a unique key from request parameters."""
    stable = json.dumps(prefs, sort_keys=True)
    return hashlib.md5(stable.encode()).hexdigest()


def _get_cached(key: str) -> dict | None:
    """Return cached response if it exists and hasn't expired."""
    if key in _cache:
        timestamp, data = _cache[key]
        if time.time() - timestamp < CACHE_TTL_SECONDS:
            return data
        del _cache[key]
    return None


def _set_cache(key: str, data: dict) -> None:
    """Store response in cache."""
    _cache[key] = (time.time(), data)


# ── Middleware ─────────────────────────────────────────────
@app.middleware("http")
async def log_and_rate_limit(request: Request, call_next):
    start = time.time()

    # Rate limiting check
    client_ip = request.client.host if request.client else "unknown"
    if _is_rate_limited(client_ip):
        logger.warning("Rate limited: %s", client_ip)
        return JSONResponse(
            status_code=429,
            content={"detail": "Too many requests. Max 30 per minute."},
        )

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
    except Exception as e:  # noqa: BLE001
        status["database"] = f"error: {e}"
        logger.error("Database health check failed: %s", e)

    # Check model
    try:
        from src.models.predict import MODEL_PATH
        if MODEL_PATH.exists():
            status["model"] = "ok"
        else:
            status["model"] = "not found"
    except Exception as e:  # noqa: BLE001
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

    # Check cache first
    cache_key = _get_cache_key(prefs.model_dump())
    cached = _get_cached(cache_key)
    if cached is not None:
        logger.info("Cache HIT — returning cached response")
        return RecommendationResponse(**cached)

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
        logger.error("Recommendation failed: %s", e, exc_info=True)  # noqa: G201
        raise HTTPException(status_code=500, detail=f"Internal error: {e}")

    logger.info("Returning %d recommendations (cache MISS)", len(results_df))
    recommendations = [Recommendation(**row) for row in results_df.to_dict(orient="records")]
    response = RecommendationResponse(recommendations=recommendations)

    # Store in cache
    _set_cache(cache_key, response.model_dump())

    return response


@app.get("/destinations/{destination_id}")
def get_destination(destination_id: int) -> dict:
    return {"id": destination_id, "name": "TODO: fetch from database"}


@app.get("/states/{state_name}/destinations")
def get_state_destinations(state_name: str, limit: int = 12, offset: int = 0) -> dict:
    """Places to visit in one state, most popular first (used by Explore India)."""
    from sqlalchemy import text

    from src.db.connection import engine

    limit = max(1, min(limit, 50))
    offset = max(0, offset)
    params = {"state": state_name, "limit": limit, "offset": offset}

    with engine.connect() as conn:
        total = conn.execute(
            text(
                "SELECT COUNT(*) FROM destinations "
                "WHERE lower(replace(state, '&', 'and')) "
                "= lower(replace(:state, '&', 'and'))"
            ),
            params,
        ).scalar()

        rows = (
            conn.execute(
                text(
                    "SELECT destination_id, name, city, state, type, significance, "
                    "avg_rating, entrance_fee_inr, time_needed_hrs, category "
                    "FROM destinations "
                    "WHERE lower(replace(state, '&', 'and')) "
                    "= lower(replace(:state, '&', 'and')) "
                    "ORDER BY COALESCE(avg_rating, 0) "
                    "* ln(1 + COALESCE(num_reviews, 0)) DESC, destination_id "
                    "LIMIT :limit OFFSET :offset"
                ),
                params,
            )
            .mappings()
            .all()
        )

    return {
        "state": state_name,
        "total": int(total or 0),
        "destinations": [dict(row) for row in rows],
    }
from src.api.accounts import router as accounts_router

app.include_router(accounts_router)
