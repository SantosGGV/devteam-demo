from main import app
import pytest
from fastapi.testclient import TestClient

client = TestClient(app)

def test_obtener_carta():
    response = client.get("/carta")
    assert response.status_code == 200

def test_crear_plato():
    plato = {"id": 1, "nombre": "Pasta", "descripcion": "Pasta con salsa de tomate", "precio": 10.99}
    response = client.post("/plato", json=plato)
    assert response.status_code == 201

def test_crear_reserva():
    reserva = {"id": 1, "nombre": "Juan", "fecha": "2024-09-16", "hora": "20:00"}
    response = client.post("/reserva", json=reserva)
    assert response.status_code == 201