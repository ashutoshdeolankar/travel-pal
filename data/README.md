# Data — schema & sources

Phase 1 scope: India-only, destinations + accommodations (food/restaurants can follow in a later iteration). Raw CSVs go in `data/raw/` (git-ignored) and get loaded via `src/data/load_data.py`.

## `destinations` (raw source: Kaggle "Travel Dataset: Guide to India's Must See Places")
| field (target, post-cleaning) | raw column in source CSV | type | notes |
|---|---|---|---|
| id | _(generate — no id in source)_ | int | assign on load |
| name | Name | string | |
| city | City | string | |
| state | State | string | |
| zone | Zone | categorical | Northern / Southern / etc. |
| type | Type | categorical | Temple / War Memorial / Natural Park / etc. |
| avg_rating | Google review rating | float | 0–5 |
| num_reviews | Number of google review in lakhs | float | popularity proxy |
| entrance_fee_inr | Entrance Fee in INR | float | used for budget filtering |
| time_needed_hrs | time needed to visit in hrs | float | feeds itinerary planning (Phase 12) |
| significance | Significance | categorical | Historical / Religious / Environmental / etc. |
| best_time_to_visit | Best time to visit | string | |

## `accommodations` (raw source: Kaggle "India's Airbnb Gems 2024")
| field (target, post-cleaning) | raw column in source CSV | type | notes |
|---|---|---|---|
| id | _(generate — no id in source)_ | int | assign on load |
| name | name | string | |
| address | address | string | |
| lat, lon | location/lat, location/lng | float | for future distance-to-destination matching |
| price_per_night | pricing/rate/amount | float | used for budget filtering |
| avg_rating | stars | float | |
| num_guests | numberOfGuests | int | |
| room_type | roomType | categorical | |
| is_superhost | isHostedBySuperhost | bool | possible quality signal |

Note: this accommodations dataset isn't linked to specific destinations by ID — Phase 2 will need a step to associate listings with the nearest destination (e.g. by city name match, or lat/lon distance once both have coordinates).

## `restaurants`
| field | type | notes |
|---|---|---|
| id | string/int | primary key |
| destination_id | FK → destinations.id | |
| name | string | |
| cuisine_type | categorical | |
| price_bucket | categorical | |
| avg_rating | float | |

## `reviews` (optional for v1)
| field | type | notes |
|---|---|---|
| id | string/int | primary key |
| target_type | categorical | destination / hotel / restaurant |
| target_id | FK | |
| rating | float | |
| text | text | |

## `user_preferences` (captured per request, not necessarily persisted in v1)
| field | type | notes |
|---|---|---|
| budget | categorical/float | |
| duration_days | int | |
| interests | list[string] | e.g. ["beach", "food", "hiking"] |

## Sources

- [x] **Destinations**: Kaggle — "Travel Dataset: Guide to India's Must See Places" (`saketk511/travel-dataset-guide-to-indias-must-see-places`). Check the dataset page for its license before publishing/redistributing.
- [x] **Accommodations**: Kaggle — "India's Airbnb Gems 2024: Trending Picks" (`kanchana1990/indias-airbnb-gems-2024-trending-picks`). Author states it was collected respecting Airbnb's platform terms — still confirm the license on the dataset page before any redistribution.
- [ ] **Restaurants/food** — not sourced yet, planned as a later addition.
