from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_low_energy_recommendation():
    payload = {
        "mood": 2,
        "energy": 1,
        "stress": 5,
        "available_time": 30
    }

    response = client.post("/recommend", json=payload)
    data = response.json()

    assert response.status_code == 200
    assert "Light task" in data["task"]


def test_high_performance_recommendation():
    payload = {
        "mood": 5,
        "energy": 5,
        "stress": 1,
        "available_time": 90
    }

    response = client.post("/recommend", json=payload)
    data = response.json()

    assert response.status_code == 200
    assert "Deep work" in data["task"]
