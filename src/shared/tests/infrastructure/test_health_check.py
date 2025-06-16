from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_return_200_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"detail": "ok"}