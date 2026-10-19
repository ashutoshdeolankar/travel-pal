"""Make a tiny fake dataset so CI can train and test without the real data."""

import argparse
import random
from pathlib import Path

import pandas as pd

# (type, significance, how many, possible entrance fees)
GROUPS = [
    ("Hindu temple", "Religious", 20, [0]),
    ("Fort", "Historical", 10, [0, 20, 25, 50, 100]),
    ("Museum", "Historical", 8, [20, 50, 100]),
    ("Beach", "Natural", 10, [0, 0, 20]),
    ("National park", "Natural", 6, [50, 100, 200]),
    ("Adventure sports center", "Recreational", 6, [100, 200, 500]),
]
PLACES = [
    ("Jaipur", "Rajasthan"),
    ("Varanasi", "Uttar Pradesh"),
    ("Goa", "Goa"),
    ("Udaipur", "Rajasthan"),
    ("Mysuru", "Karnataka"),
    ("Kochi", "Kerala"),
]


def main(out_dir: Path) -> None:
    dest_file = out_dir / "destinations_clean.csv"
    acc_file = out_dir / "accommodations_clean.csv"
    if dest_file.exists() or acc_file.exists():
        raise SystemExit(f"{out_dir} already has data files. Refusing to overwrite.")

    rng = random.Random(42)
    items = []
    for type_, significance, count, fees in GROUPS:
        for _ in range(count):
            items.append((type_, significance, rng.choice(fees)))
    rng.shuffle(items)

    rows = []
    for i, (type_, significance, fee) in enumerate(items, start=1):
        city, state = PLACES[i % len(PLACES)]
        score = round(rng.uniform(0.3, 0.95), 3)
        rows.append(
            {
                "destination_id": i,
                "name": f"Sample {type_} {i}",
                "city": city,
                "state": state,
                "type": type_,
                "significance": significance,
                "avg_rating": round(rng.uniform(3.8, 4.9), 1),
                "num_reviews": rng.randint(50, 5000),
                "entrance_fee_inr": fee,
                "time_needed_hrs": float(rng.randint(1, 3)),
                "best_time_to_visit": "Oct-Mar",
                "latitude": 20.0 + i * 0.1,
                "longitude": 75.0 + i * 0.1,
                "human_label": None,
                "hidden_gem_score": score,
                "category": "Hidden Gem" if score > 0.6 else "Well-Known",
            }
        )

    accommodations = [
        {
            "address": f"{i} Sample Road",
            "isHostedBySuperhost": i % 2 == 0,
            "location": PLACES[i % len(PLACES)][0],
            "name": f"Sample Stay {i}",
            "numberOfGuests": 2 + i % 3,
            "pricing": 1500 + i * 100,
            "roomType": "Entire home",
            "stars": 4.0,
        }
        for i in range(1, 11)
    ]

    out_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(dest_file, index=False)
    pd.DataFrame(accommodations).to_csv(acc_file, index=False)
    print(f"Wrote {len(rows)} destinations and {len(accommodations)} stays to {out_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data/processed")
    main(Path(parser.parse_args().out))