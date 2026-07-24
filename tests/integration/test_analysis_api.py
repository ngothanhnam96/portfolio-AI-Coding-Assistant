from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_analyze_endpoint_returns_result() -> None:
    response = client.post(
        "/api/v1/analyze",
        json={
            "task": "explain_code",
            "language": "python",
            "code": "def add(a, b):\n    return a + b",
        },
    )

    assert response.status_code == 200
    assert response.json()["task"] == "explain_code"
