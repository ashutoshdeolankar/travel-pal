import pandas as pd

from src.db.state_fixes import clean_locations, fix_unknown_states


def _frame():
    return pd.DataFrame(
        {
            "city": ["Leh", "Gulmarg", "Jerez", "Jaipur", "Jammu"],
            "state": ["Unknown", "Unknown", "Unknown", "Rajasthan", "Punjab"],
        }
    )


def test_known_cities_get_their_state():
    fixed = fix_unknown_states(_frame())
    assert fixed.loc[0, "state"] == "Ladakh"
    assert fixed.loc[1, "state"] == "Jammu and Kashmir"


def test_unlisted_city_stays_unknown():
    fixed = fix_unknown_states(_frame())
    assert fixed.loc[2, "state"] == "Unknown"


def test_places_with_a_real_state_are_not_touched():
    fixed = fix_unknown_states(_frame())
    assert fixed.loc[3, "state"] == "Rajasthan"
    assert fixed.loc[4, "state"] == "Punjab"


def test_original_table_is_not_changed():
    original = _frame()
    fix_unknown_states(original)
    assert original.loc[0, "state"] == "Unknown"


def test_places_outside_india_are_removed():
    cleaned = clean_locations(_frame())
    assert "Jerez" not in cleaned["city"].tolist()
    assert len(cleaned) == 4


def test_rows_are_renumbered_after_removal():
    cleaned = clean_locations(_frame())
    assert cleaned.index.tolist() == [0, 1, 2, 3]


def test_a_real_state_protects_a_place_from_removal():
    frame = pd.DataFrame({"city": ["Jerez"], "state": ["Kerala"]})
    assert len(clean_locations(frame)) == 1