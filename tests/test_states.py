import pytest
from fastapi.testclient import TestClient

from src.api import main as api_main

client = TestClient(api_main.app)


@pytest.fixture(autouse=True)
def clean_rate_counter():
    api_main._rate_tracker.clear()
    yield
    api_main._rate_tracker.clear()


def test_state_returns_places_from_that_state():
    response = client.get("/states/Rajasthan/destinations")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] > 0
    assert len(data["destinations"]) > 0
    assert all(d["state"] == "Rajasthan" for d in data["destinations"])


def test_state_name_is_not_case_sensitive():
    upper = client.get("/states/RAJASTHAN/destinations").json()
    lower = client.get("/states/rajasthan/destinations").json()
    assert upper["total"] == lower["total"]
    assert upper["total"] > 0


def test_limit_and_offset_give_different_pages():
    first = client.get("/states/Rajasthan/destinations?limit=3").json()
    second = client.get("/states/Rajasthan/destinations?limit=3&offset=3").json()
    assert len(first["destinations"]) <= 3
    first_ids = {d["destination_id"] for d in first["destinations"]}
    second_ids = {d["destination_id"] for d in second["destinations"]}
    assert first_ids.isdisjoint(second_ids)


def test_limit_is_capped_at_50():
    data = client.get("/states/Rajasthan/destinations?limit=1000").json()
    assert len(data["destinations"]) <= 50


def test_unknown_state_gives_empty_list():
    response = client.get("/states/Atlantis/destinations")
    assert response.status_code == 200
    assert response.json() == {"state": "Atlantis", "total": 0, "destinations": []}