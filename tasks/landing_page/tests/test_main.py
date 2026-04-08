from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Landing Page" in response.text
    assert "Hero Section" in response.text
    assert "Feature 1" in response.text
    assert "Feature 2" in response.text
    assert "Feature 3" in response.text
    assert "2023 Landing Page. Todos los derechos reservados." in response.text