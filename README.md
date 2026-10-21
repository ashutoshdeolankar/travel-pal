# Travel Pal

An MLOps-based smart travel recommendation system for India. You give it a budget, trip length and interests (for example "Temple"), and it returns the best-matching places from a database of about 9,000 destinations (9,003 after cleaning).

See `docs/Travel_Pal_Build_Roadmap.md` (or the team's shared roadmap doc) for the full phase-by-phase build plan.

## Team
- Nandini Dahale – AI3107
- Ashutosh Deolankar – AI3109
- Akshay Deshpande – AI3110
- Arpita Deshpande – AI3111

## Status
Phases 0 to 11 are working: data pipeline, trained model, PostgreSQL, FastAPI, Docker, CI on GitHub Actions, request logging, caching, rate limiting, tests, and a frontend connected to the API. Production deployment and scaling (Phase 12) are not started.

## How it works

1. **Data** is cleaned and loaded into PostgreSQL.
2. **Model:** each place becomes a vector (its type and significance, plus its rating and review count). The user's interests become a vector too, and places are ranked by cosine similarity.
3. **API (FastAPI)** serves recommendations and state-wise place lists. Answers are cached for 5 minutes, and each IP address is limited to 30 requests per minute.
4. **Frontend** (`frontend/`) is a static website that calls the API.

## Project structure

```
travel-pal/
├── data/
│   ├── raw/              # untouched scraped/downloaded data (git-ignored, kept locally or via DVC)
│   └── processed/        # cleaned, feature-engineered data and the trained model (git-ignored)
├── notebooks/            # exploratory Jupyter notebooks (EDA, prototyping)
├── src/
│   ├── data/             # scraping / data-loading scripts
│   ├── features/         # feature engineering and preprocessing
│   ├── models/           # training + inference code
│   ├── db/               # database connection and loading
│   ├── api/              # FastAPI app
│   └── pipelines/        # Prefect/Airflow flows for retraining
├── frontend/             # index.html, state.html, assets/ (videos and images)
├── scripts/              # make_sample_data.py (small fake dataset used by CI)
├── tests/                # pytest tests
├── docker/               # Dockerfile + docker-compose.yml
├── .github/workflows/    # CI/CD (GitHub Actions)
├── mlruns/               # local MLflow tracking store (git-ignored)
├── requirements.txt
└── README.md
```

## Getting started (local dev)

Requirements: Python 3.11, PostgreSQL 16 (or Docker), Git.

1. **Clone and create a virtual environment**
   ```bash
   git clone <repo-url> travel-pal
   cd travel-pal
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Set the database connection.** Create a `.env` file in the project root (it is git-ignored):
   ```
   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/travelpal
   ```

3. **Get the data.** The datasets and the trained model are not stored in Git. Put the raw files in `data/raw/` as described in `data/README.md`, then run the pipeline from the project root:
   ```bash
   python -m src.features.preprocess    # clean the raw data
   python -m src.models.train           # train the model, log to MLflow
   python -m src.db.load_to_db          # load cleaned data into PostgreSQL
   ```
   Warning: `load_to_db` replaces the `destinations` and `accommodations` tables.

   Both `train` and `load_to_db` apply the same location cleaning (`src/db/state_fixes.py`): a few cities saved with the state "Unknown" get their real state, and places outside India (Jerez in Spain, Delicias in Mexico) are removed. The model finds a place by its row position, so **whenever you retrain, reload the database too** (and the other way round). `tests/test_model_alignment.py` fails if the two disagree.

4. **Run the API locally**
   ```bash
   uvicorn src.api.main:app --reload
   ```
   Then open http://127.0.0.1:8000/docs for the interactive API docs, and http://127.0.0.1:8000/health to check the API, database and model.

5. **Run tests and lint**
   ```bash
   ruff check src/ tests/
   pytest -v
   ```
   The recommendation and state tests need the model file and the database to be loaded.

6. **Track experiments with MLflow**
   ```bash
   mlflow ui
   ```
   Then open http://127.0.0.1:5000.

## Full stack with Docker

```bash
docker compose -f docker/docker-compose.yml up -d
```

This starts the API (port 8000) and PostgreSQL. To run the pipeline inside the container:

```bash
docker exec -it docker-api-1 python -m src.features.preprocess
docker exec -it docker-api-1 python -m src.models.train
docker exec -it docker-api-1 python -m src.db.load_to_db
```

Useful commands: `docker compose -f docker/docker-compose.yml logs api --tail 50` to read logs, `... restart api` after changing code, `... down` to stop.

## API

| Method and path | Purpose |
|---|---|
| `GET /health` | status of the API, database and model |
| `POST /recommendations` | best-matching places for a trip |
| `GET /states/{state}/destinations?limit=12&offset=0` | top-rated places of one state, paged (limit is capped at 50) |
| `GET /destinations/{id}` | placeholder, not implemented yet |

Example request:

```bash
curl -X POST http://localhost:8000/recommendations \
  -H "Content-Type: application/json" \
  -d '{"budget":"mid","duration_days":5,"interests":["Temple"],"top_n":5}'
```

| Field | Values |
|---|---|
| `budget` | `low` (entrance fee up to 20 rupees), `mid` (up to 50 rupees) or `high` (no limit) |
| `duration_days` | 1 or more |
| `interests` | a list such as `["Temple", "Historical"]`; words like temple, fort, beach and wildlife are mapped to the model's categories; an empty list ranks by rating |
| `top_n` | 1 to 50 (default 10) |
| `category` | `all`, `hidden_gem` or `well_known` |

## Frontend

1. Start the API (see above).
2. Open `frontend/index.html` in a browser.

The trip planner calls `POST /recommendations`. Each state page in Explore India calls the state endpoint to list more places. If the API is not running, the planner shows a message and the extra sections stay hidden.

## CI (GitHub Actions)

`.github/workflows/ci.yml` runs on every push to `main` and on pull requests:

1. **lint:** `ruff`
2. **test:** starts a temporary PostgreSQL, builds a small fake dataset with `scripts/make_sample_data.py`, trains a model on it, loads it, and runs all tests
3. **docker-build:** builds the Docker image

## Branching convention

- `main` — always deployable.
- `feature/<short-description>` — one branch per feature, merged via pull request.
- Run lint and tests locally (`ruff check src/ tests/` and `pytest`) before opening a PR; CI will also run them automatically.

## Known limitations

- **Budget is only a rough filter.** Entrance fees in the data are between 0 and 100 rupees (44% of places are free), so the budget bands only hide the few more expensive places. A real "can I afford this trip" check would need hotel, food and transport costs; the accommodation data (500 listings, most states with fewer than 10) is too thin to estimate them reliably.
- The "Hidden Gem" classifier has low accuracy (about 55% on a small test set).
- Jammu and Kashmir (112 places) and Ladakh (29 places) are found only through the cities listed in `src/db/state_fixes.py`, and one place (Manakpur Kholgaman) still has the state "Unknown".
- The Trip Reality Score and the day-by-day itinerary on the website are demonstration logic.
- The cache and rate limiter live in the API's memory, so they reset when the API restarts.

## Team ownership (suggested starting split)

| Area | Owner | Phase(s) |
|---|---|---|
| Data collection & sourcing | TBD | 1 |
| Preprocessing / EDA / feature engineering | TBD | 2 |
| Model & MLflow tracking | TBD | 3–4 |
| API & database | TBD | 5–6 |
| Docker, CI/CD, deployment, monitoring | TBD | 7–11 |

Fill in owners once the team splits up the first tasks.
