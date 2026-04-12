import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_crear_reserva():
    response = client.post('/reserva', json={'nombre': 'Juan', 'fecha': '2024-01-01', 'hora': '10:00'})
    assert response.status_code == 200
    assert response.json() == {'confirmación': 'reserva creada'}

def test_crear_reserva_invalida():
    response = client.post('/reserva', json={'nombre': 'Juan'})
    assert response.status_code == 422
