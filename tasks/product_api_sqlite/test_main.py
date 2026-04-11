from main import app, session, Producto
import pytest
from fastapi.testclient import TestClient

client = TestClient(app)

def test_obtener_productos():
    # Limpiar la base de datos
    session.query(Producto).delete()
    session.commit()

    # Crear algunos productos
    producto1 = Producto(nombre="Producto 1", precio=10.99, stock=10)
    producto2 = Producto(nombre="Producto 2", precio=5.99, stock=20)
    session.add_all([producto1, producto2])
    session.commit()

    # Obtener los productos
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_crear_producto():
    # Limpiar la base de datos
    session.query(Producto).delete()
    session.commit()

    # Crear un nuevo producto
    response = client.post("/products", json={"nombre": "Producto 3", "precio": 7.99, "stock": 15})
    assert response.status_code == 201
    assert response.json()["mensaje"] == "Producto creado con éxito"

def test_obtener_producto():
    # Limpiar la base de datos
    session.query(Producto).delete()
    session.commit()

    # Crear un producto
    producto = Producto(nombre="Producto 4", precio=8.99, stock=12)
    session.add(producto)
    session.commit()

    # Obtener el producto
    response = client.get(f"/products/{producto.id}")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Producto 4"

def test_actualizar_producto():
    # Limpiar la base de datos
    session.query(Producto).delete()
    session.commit()

    # Crear un producto
    producto = Producto(nombre="Producto 5", precio=9.99, stock=10)
    session.add(producto)
    session.commit()

    # Actualizar el producto
    response = client.put(f"/products/{producto.id}", json={"nombre": "Producto 5 actualizado", "precio": 10.99, "stock": 15})
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Producto actualizado con éxito"

def test_eliminar_producto():
    # Limpiar la base de datos
    session.query(Producto).delete()
    session.commit()

    # Crear un producto
    producto = Producto(nombre="Producto 6", precio=11.99, stock=12)
    session.add(producto)
    session.commit()

    # Eliminar el producto
    response = client.delete(f"/products/{producto.id}")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Producto eliminado con éxito"