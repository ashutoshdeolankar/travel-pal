# Travel Pal – Data

This folder holds the data used by Travel Pal. The raw files are **not stored in git**
(they are large and listed in `.gitignore`), so you must download them once and put them
in `data/raw/` before running the pipeline.

## Folder layout

```
data/
  raw/        <- you put the 2 downloaded CSV files here (not in git)
  processed/  <- created by the preprocessing step (not in git)
```

## Raw files

| File (exact name) | Size | What it contains |
|---|---|---|
| `travelpal_india_combined_v2.csv` | ~24 MB | Tourist places in India (about 15,000 rows before cleaning). |
| `india_airbnb_listings.csv` | ~58 KB | Stays / accommodation listings (500 rows used). |

### Where the data came from

- **`travelpal_india_combined_v2.csv`** was put together by our team by combining several
  public sources: Kaggle datasets, GitHub datasets and public travel websites. We merged
  them into one file with a common set of columns.
- **`india_airbnb_listings.csv`** comes from a public GitHub dataset of Airbnb-style listings.

Please check the licence of each original source before reusing the data outside this
college project.

### Main columns in the places file

`destination_id, name, city, state, country, category, subcategory, rating, reviews_count,
description, tags, best_time, latitude, longitude, address`

### How to get the files

The files are shared with the team through the GitHub repository (see the repo's
**Releases** page, or ask the team for the link):

1. Download both CSV files.
2. Copy them into `data/raw/` with exactly the names above.

## Run order (after the files are in `data/raw/`)

Run these from the project root with the virtual environment active:

```powershell
python -m src.features.preprocess     # clean the raw files -> data/processed/
python -m src.models.train            # train the recommender (also logs to MLflow)
docker compose -f docker/docker-compose.yml up -d db   # start PostgreSQL
python -m src.db.load_to_db           # load cleaned data into the database
```

Important: the trained model finds places by **row position**, so the model and the
database must be built from the same cleaned data, in the same order. If you re-run
`preprocess`, re-run `train` and `load_to_db` too. `tests/test_model_alignment.py`
checks this.

## What the cleaning step does

- Drops rows with no rating, category or city.
- Drops business/service rows that are not places to visit (travel agencies, hotels, taxi
  services, government offices and similar).
- Removes duplicates (same name in the same city).
- Fills a missing state from the city when possible; places still unknown are labelled
  `Unknown`. A few known cities are fixed by hand (`src/db/state_fixes.py`).
- Removes places that are not in India (98 rows were removed).
- Creates a `significance` tag (Religious, Historical, Natural, Recreational, General)
  from keywords in the name, category and description.
- Tags each place Hidden Gem or Well-Known from its rating and number of reviews.

After cleaning, the database has **9,003 destinations** and **500 accommodations**.

## Important: some columns are estimates, not real data

`entrance_fee_inr` and `time_needed_hrs` are **not in the source data**. They are
**estimated from the place's `significance` tag** in `src/features/preprocess.py`
(for example, religious places are mostly free, some historical places get a small fee).

Because of this:

- Treat these values as rough guesses, not real ticket prices or visit times.
- The budget filter (low = fee up to ₹20, mid = up to ₹50, high = no limit) and the
  trip-duration filter are based on these estimates.

The **Hidden Gem / Well-Known** classifier only reaches about 55% accuracy (close to a
coin flip), so the website does not show that label to users.
