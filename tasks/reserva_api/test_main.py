from main import app
import pytest
from fastapi.testclient import TestClient

client = TestClient(app)

def test_crear_reserva():
    respuesta = client.post("/reserva", json={"nombre": "Juan", "fecha": "2024-09-16", "hora": "10:00"})
    assert respuesta.status_code == 201
    assert respuesta.json() == {"mensaje": "Reserva creada con éxito"}

def test_crear_reserva_sin_nombre():
    respuesta = client.post("/reserva", json={"fecha": "2024-09-16", "hora": "10:00"})
    assert respuesta.status_code == 422

def test_crear_reserva_sin_fecha():
    respuesta = client.post("/reserva", json={"nombre": "Juan", "hora": "10:00"})
    assert respuesta.status_code == 422

def test_crear_reserva_sin_hora():
    respuesta = client.post("/reserva", json={"nombre": "Juan", "fecha": "2024-09-16"})
    assert respuesta.status_code == 422