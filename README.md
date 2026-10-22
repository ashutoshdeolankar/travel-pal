# Vishwaara

> Vishwaara was called *Travel Pal* earlier. The GitHub repository and the internal names (`travelpal` database, Docker names) still use the old name.

An MLOps-based smart travel recommendation system for India. You give it a budget, trip length and interests (for example "Temple"), and it returns the best-matching places from a database of about 9,000 destinations (9,003 after cleaning).

See `docs/Travel_Pal_Build_Roadmap.md` (or the team's shared roadmap doc) for the full phase-by-phase build plan.

## Team
- Nandini Dahale – AI3107
- Ashutosh Deolankar – AI3109
- Akshay Deshpande – AI3110
- Arpita Deshpande – AI3111

## Status
Phases 0 to 11 are working: data pipeline, trained model, PostgreSQL, FastAPI, Docker, CI on GitHub Actions, request logging, caching, rate limiting, tests, a frontend connected to the API, and user accounts (sign up, log in, saved trips, favourite places). Production deployment and scaling (Phase 12) are not started.

## How it works

1. **Data** is cleaned and loaded into PostgreSQL.
2. **Model:** each place becomes a vector (its type and significance, plus its rating and review count). The user's interests become a vector too, and places are ranked by cosine similarity.
3. **API (FastAPI)** serves recommendations and state-wise place lists. Answers are cached for 5 minutes, and each IP address is limited to 30 requests per minute.
4. **Frontend** (`frontend/`) is a static website that calls the API.
5. **Accounts** (`src/api/accounts.py`): people can sign up, log in, save generated trips and favourite places in PostgreSQL. A human check (a signed maths question) protects sign-up and login.

## Project structure

```
vishwaara/
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
├── frontend/             # index.html, state.html, login.html, my-trips.html, auth.js, plans.js, assets/
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
   git clone <repo-url> vishwaara
   cd vishwaara
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Set the database connection.** Create a `.env` file in the project root (it is git-ignored):
   ```
   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/travelpal
   ```

3. **Get the data.** The datasets and the trained model are not stored in Git. Download the two raw CSV files from the [data-v1 release](https://github.com/ashutoshdeolankar/vishwaara/releases/tag/data-v1), put them in `data/raw/` (details in `data/README.md`), then run the pipeline from the project root:
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
| `GET /auth/captcha` | a new human-check question (or the Google reCAPTCHA site key, if switched on) |
| `POST /auth/register`, `POST /auth/login` | create an account / log in (both need the human check); return a session token |
| `GET /auth/me`, `PUT /auth/me`, `POST /auth/logout` | read or update the profile, log out (Bearer token) |
| `GET /trips`, `POST /trips`, `DELETE /trips/{id}` | saved trips of the logged-in user |
| `GET /favourites`, `POST /favourites`, `DELETE /favourites/{id}` | favourite places of the logged-in user |

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

## Accounts and saved data

- **Tables** (created automatically on first use): `users`, `sessions`, `saved_trips`, `favourites`. Deleting a user deletes their sessions, trips and favourites.
- **Passwords** are never stored. Only a salted `scrypt` hash is kept. A login gives a random session token (valid 7 days); only its SHA-256 hash is stored.
- **Human check:** `/auth/captcha` returns a small maths question with a signed, one-time, 5-minute token. No keys or internet are needed. Optionally, the real Google reCAPTCHA (v2 checkbox) can be switched on by putting `RECAPTCHA_SITE_KEY` and `RECAPTCHA_SECRET_KEY` in `docker/.env` (git-ignored). The website then shows Google's "I'm not a robot" box, and it must be opened from `http://localhost`.
- **Limits:** 200 saved trips and 500 favourites per user; one saved trip may not exceed 200 KB.
- **To look at the stored accounts:**
  ```bash
  docker exec docker-db-1 psql -U travelpal -d travelpal -c "SELECT id, name, email, created_at FROM users;"
  ```

## Frontend

1. Start the API (see above).
2. Open `frontend/index.html` in a browser (or run `python -m http.server 5500 --directory frontend` and open http://localhost:5500).

Pages: `index.html` (home, trip planner, Explore India), `state.html` (one state: photo, places, four ready-made travel plans), `login.html` (sign up / log in), `my-trips.html` (profile, saved trips, favourites).

The trip planner calls `POST /recommendations` and, when a destination state is chosen, `GET /states/{state}/destinations` to suggest spots. It builds a time-based day-by-day itinerary in the browser (opening hours, lunch break, travel buffers). A logged-in user can save the trip and mark places as favourites. Each state page in Explore India calls the state endpoint to list more places. If the API is not running, the planner shows a message and the extra sections stay hidden.

## CI (GitHub Actions)

`.github/workflows/ci.yml` runs on every push to `main` and on pull requests:

1. **lint:** `ruff`
2. **test:** starts a temporary PostgreSQL (the account tests also use it), builds a small fake dataset with `scripts/make_sample_data.py`, trains a model on it, loads it, and runs all tests
3. **docker-build:** builds the Docker image

## Branching convention

- `main` — always deployable.
- `feature/<short-description>` — one branch per feature, merged via pull request.
- Run lint and tests locally (`ruff check src/ tests/` and `pytest`) before opening a PR; CI will also run them automatically.

## Known limitations

- **Budget is only a rough filter.** Entrance fees (and visit times) are **estimates**, not scraped values: `preprocess.py` guesses them from each place's type (religious, historical, natural and so on), so they range only from 0 to 100 rupees (44% of places are free). The budget bands therefore only hide the few places estimated as more expensive. A real "can I afford this trip" check would need hotel, food and transport costs; the accommodation data (500 listings, most states with fewer than 10) is too thin to estimate them reliably.
- The "Hidden Gem" classifier has low accuracy (about 55% on a small test set).
- Jammu and Kashmir (112 places) and Ladakh (29 places) are found only through the cities listed in `src/db/state_fixes.py`, and one place (Manakpur Kholgaman) still has the state "Unknown".
- The Trip Reality Score is demonstration logic. The itinerary uses the *estimated* visit times, and the prices in the ready-made travel plans (`frontend/plans.js`) are rough sample figures written from general knowledge, not live quotes.
- Accounts are a basic implementation for this project: no email verification and no password reset.
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
