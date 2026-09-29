from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["service"] == "cloud-reliability-lab"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ready():
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_info():
    response = client.get("/info")

    assert response.status_code == 200
    assert response.json()["service"] == "cloud-reliability-lab"
    assert response.json()["version"] == "0.1.0"
