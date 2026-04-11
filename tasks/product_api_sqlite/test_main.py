from main import app, session, Producto
import pytest
from fastapi.testclient import TestClient

client = TestClient(app)

def test_obtener_productos():
    # Limpiar la base de datos
    session.query(Producto).delete()
    session.commit()
    
    # Crear un producto
    nuevo_producto = Producto(nombre="Prueba", precio=10.99, stock=5)
    session.add(nuevo_producto)
    session.commit()
    
    # Obtener los productos
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["nombre"] == "Prueba"

def test_crear_producto():
    # Limpiar la base de datos
    session.query(Producto).delete()
    session.commit()
    
    # Crear un nuevo producto
    response = client.post("/products", json={"nombre": "Prueba", "precio": 10.99, "stock": 5})
    assert response.status_code == 201
    assert response.json()["mensaje"] == "Producto creado con éxito"
    
    # Comprobar que el producto se ha creado
    productos = session.query(Producto).all()
    assert len(productos) == 1
    assert productos[0].nombre == "Prueba"