import pandas as pd

from src.models.predict import _apply_budget_duration_filter


def _places():
    return pd.DataFrame(
        {
            "name": ["free", "cheap", "fifty", "pricey", "long"],
            "entrance_fee_inr": [0, 20, 50, 100, 0],
            "time_needed_hrs": [1, 2, 3, 2, 30],
        }
    )


def test_low_budget_allows_fees_up_to_20_rupees():
    result = _apply_budget_duration_filter(_places(), "low", 5)
    assert set(result["name"]) == {"free", "cheap", "long"}


def test_mid_budget_allows_fees_up_to_50_rupees():
    result = _apply_budget_duration_filter(_places(), "mid", 5)
    assert set(result["name"]) == {"free", "cheap", "fifty", "long"}


def test_high_budget_has_no_fee_limit():
    result = _apply_budget_duration_filter(_places(), "high", 5)
    assert len(result) == 5


def test_short_trip_drops_places_that_need_too_many_hours():
    result = _apply_budget_duration_filter(_places(), "high", 1)
    assert "long" not in set(result["name"])


def test_original_table_is_not_changed():
    places = _places()
    _apply_budget_duration_filter(places, "low", 1)
    assert len(places) == 5