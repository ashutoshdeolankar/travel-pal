from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_recommendations_returns_results():
    payload = {"budget": "mid", "duration_days": 5, "interests": ["beach", "food"]}
    response = client.post("/recommendations", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "recommendations" in body
    assert len(body["recommendations"]) > 0
