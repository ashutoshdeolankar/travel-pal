from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def _ask(**overrides):
    body = {"budget": "mid", "duration_days": 5, "interests": ["Temple"], "top_n": 5}
    body.update(overrides)
    return client.post("/recommendations", json=body)


def test_temple_gives_religious_places():
    response = _ask()
    assert response.status_code == 200
    results = response.json()["recommendations"]
    assert len(results) == 5
    religious = [r for r in results if r["significance"] == "Religious"]
    assert len(religious) >= 3


def test_empty_interests_still_works():
    response = _ask(interests=[])
    assert response.status_code == 200
    assert len(response.json()["recommendations"]) == 5


def test_unknown_interest_does_not_crash():
    response = _ask(interests=["zzzxxx"])
    assert response.status_code == 200


def test_top_n_is_respected():
    response = _ask(top_n=3)
    assert len(response.json()["recommendations"]) == 3