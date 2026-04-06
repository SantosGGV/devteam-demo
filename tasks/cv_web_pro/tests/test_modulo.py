import pytest
from fastapi.testclient import TestClient
from modulo import app

class TestApp:
    def test_root(self):
        client = TestClient(app)
        response = client.get("/")
        assert response.status_code == 200
        assert "Santos Gómez" in response.text
        assert "Field IT Specialist" in response.text