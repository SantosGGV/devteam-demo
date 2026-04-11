from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_hello():
    response = client.get("/hello?name=Alice")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Alice!"}