# Travel Pal

An MLOps-based smart travel recommendation system. See `docs/Travel_Pal_Build_Roadmap.md` (or the team's shared roadmap doc) for the full phase-by-phase build plan.

## Team
- Nandini Dahale – AI3107
- Ashutosh Deolankar – AI3109
- Akshay Deshpande – AI3110
- Arpita Deshpande – AI3111

## Status
🚧 Phase 0 — project scaffold. Nothing is implemented yet; this is the skeleton the team builds into.

## Project structure

```
travel-pal/
├── data/
│   ├── raw/              # untouched scraped/downloaded data (git-ignored, kept locally or via DVC)
│   └── processed/        # cleaned, feature-engineered data
├── notebooks/            # exploratory Jupyter notebooks (EDA, prototyping)
├── src/
│   ├── data/              # scraping / data-loading scripts
│   ├── features/          # feature engineering
│   ├── models/            # training + inference code
│   ├── api/                # FastAPI app
│   └── pipelines/          # Prefect/Airflow flows for retraining
├── tests/                 # pytest unit tests
├── docker/                # Dockerfile + docker-compose.yml
├── .github/workflows/     # CI/CD (GitHub Actions)
├── mlruns/                 # local MLflow tracking store (git-ignored)
├── requirements.txt
└── README.md
```

## Getting started (local dev)

1. **Clone and create a virtual environment**
   ```bash
   git clone <repo-url> travel-pal
   cd travel-pal
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run the API locally**
   ```bash
   uvicorn src.api.main:app --reload
   ```
   Then open http://127.0.0.1:8000/docs for the interactive API docs, and http://127.0.0.1:8000/health to check it's alive.

3. **Run tests**
   ```bash
   pytest
   ```

4. **Track experiments with MLflow**
   ```bash
   mlflow ui
   ```
   Then open http://127.0.0.1:5000.

5. **Full stack via Docker (once Phase 6/7 are built out)**
   ```bash
   docker compose -f docker/docker-compose.yml up --build
   ```

## Branching convention

- `main` — always deployable.
- `feature/<short-description>` — one branch per feature, merged via pull request.
- Run tests locally (`pytest`) before opening a PR; CI will also run them automatically.

## Team ownership (suggested starting split)

| Area | Owner | Phase(s) |
|---|---|---|
| Data collection & sourcing | TBD | 1 |
| Preprocessing / EDA / feature engineering | TBD | 2 |
| Model & MLflow tracking | TBD | 3–4 |
| API & database | TBD | 5–6 |
| Docker, CI/CD, deployment, monitoring | TBD | 7–11 |

Fill in owners once the team splits up the first tasks.
