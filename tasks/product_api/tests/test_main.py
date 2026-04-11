from main import app
import pytest
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 3