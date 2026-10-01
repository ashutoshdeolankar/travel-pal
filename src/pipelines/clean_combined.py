"""Clean TravelPal_India_Dataset_COMBINED.csv -> destinations_clean.csv + cities_clean.csv"""
import re
import sys
import pandas as pd

SRC = sys.argv[1] if len(sys.argv) > 1 else "data/raw/TravelPal_India_Dataset_COMBINED.csv"
OUT = sys.argv[2] if len(sys.argv) > 2 else "data/processed"


def norm(s):
    s = re.sub(r"\s+", " ", str(s).lower().strip())
    return re.sub(r"[^a-z0-9 ]", "", s)


df = pd.read_csv(SRC)

# 1. trim text, blanks -> NaN
for c in df.select_dtypes(include=["object", "string"]).columns:
    df[c] = df[c].astype("string").str.strip().replace({"": pd.NA, "nan": pd.NA})
df = df.dropna(subset=["name"])
df["pincode"] = df["pincode"].astype("Int64").astype("string")

# 2. split by record type
attr = df[df.record_type == "attraction"].copy()
city = df[df.record_type == "city/town"].copy()

# 3. dedupe attractions on normalised name+city+state, keeping the fullest row
attr["_key"] = attr[["name", "city", "state"]].fillna("").apply(
    lambda r: "|".join(norm(v) for v in r), axis=1)
attr["_fill"] = attr.notna().sum(axis=1)
attr = attr.sort_values("_fill", ascending=False)
srcs = attr.groupby("_key")["source"].apply(lambda s: ", ".join(sorted(set(", ".join(s.dropna()).split(", ")))))
before = len(attr)
attr = attr.drop_duplicates("_key").copy()
attr["source"] = attr["_key"].map(srcs)
print(f"attractions: {before} -> {len(attr)} after dedupe")

# 4. helper columns for the model / API
attr["has_coordinates"] = attr.latitude.notna() & attr.longitude.notna()
attr["text_features"] = (
    attr[["name", "category", "subcategory", "category_group", "tags", "description"]]
    .fillna("").agg(" ".join, axis=1).str.replace(r"\s+", " ", regex=True).str.strip()
)
attr["has_content"] = attr[["category", "tags", "description"]].notna().any(axis=1)

attr = attr.drop(columns=["_key", "_fill", "record_type"]).sort_values("id")
city = city.drop(columns=["record_type", "pincode", "category", "subcategory", "rating",
                          "reviews_count", "city_description", "best_time",
                          "distance_from_city_km", "address", "image_url", "review_1",
                          "review_2", "tags", "city"]).sort_values("id")

import os
os.makedirs(OUT, exist_ok=True)
attr.to_csv(f"{OUT}/destinations_clean.csv", index=False)
city.to_csv(f"{OUT}/cities_clean.csv", index=False)
print("destinations:", attr.shape, "| with coords:", int(attr.has_coordinates.sum()),
      "| with content:", int(attr.has_content.sum()))
print("cities:", city.shape)
