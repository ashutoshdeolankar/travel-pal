import time

import pytest
from fastapi.testclient import TestClient

from src.api import main as api_main

client = TestClient(api_main.app)

BODY = {"budget": "mid", "duration_days": 5, "interests": ["Temple"], "top_n": 3}


@pytest.fixture(autouse=True)
def clean_state():
    """Start and finish every test with an empty cache and rate counter."""
    api_main._cache.clear()
    api_main._rate_tracker.clear()
    yield
    api_main._cache.clear()
    api_main._rate_tracker.clear()


def test_same_request_is_answered_from_cache():
    first = client.post("/recommendations", json=BODY)
    assert first.status_code == 200
    assert len(api_main._cache) == 1

    second = client.post("/recommendations", json=BODY)
    assert second.json() == first.json()
    assert len(api_main._cache) == 1


def test_different_request_gets_its_own_cache_entry():
    client.post("/recommendations", json=BODY)
    client.post("/recommendations", json={**BODY, "interests": ["Beach"]})
    assert len(api_main._cache) == 2


def test_cache_key_ignores_field_order():
    key_a = api_main._get_cache_key({"a": 1, "b": 2})
    key_b = api_main._get_cache_key({"b": 2, "a": 1})
    assert key_a == key_b


def test_expired_cache_entry_is_dropped():
    old = time.time() - api_main.CACHE_TTL_SECONDS - 1
    api_main._cache["old"] = (old, {"recommendations": []})
    assert api_main._get_cached("old") is None
    assert "old" not in api_main._cache


def test_rate_limit_blocks_after_limit():
    for _ in range(api_main.RATE_LIMIT):
        assert client.get("/destinations/1").status_code != 429
    blocked = client.get("/destinations/1")
    assert blocked.status_code == 429


def test_rate_limit_forgets_old_requests():
    long_ago = time.time() - api_main.RATE_WINDOW_SECONDS - 1
    api_main._rate_tracker["testclient"] = [long_ago] * api_main.RATE_LIMIT
    assert client.get("/destinations/1").status_code != 429


def test_rate_limit_is_per_ip():
    api_main._rate_tracker["10.0.0.9"] = [time.time()] * api_main.RATE_LIMIT
    assert client.get("/destinations/1").status_code != 429


@pytest.mark.parametrize(
    "change",
    [
        {"budget": "ultra"},
        {"duration_days": 0},
        {"top_n": 51},
        {"category": "secret"},
    ],
)
def test_bad_input_is_rejected(change):
    response = client.post("/recommendations", json={**BODY, **change})
    assert response.status_code == 422