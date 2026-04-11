from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

# Configuración de la base de datos
engine = create_engine('sqlite:///products.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Modelo de producto
class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Float)
    stock = Column(Integer)

# Esquema de producto
class ProductoSchema(BaseModel):
    nombre: str
    precio: float
    stock: int

# Crear la base de datos
Base.metadata.create_all(engine)

# Inicializar la aplicación FastAPI
app = FastAPI()

# Obtener todos los productos
@app.get("/products")
def obtener_productos():
    productos = session.query(Producto).all()
    return [{"id": p.id, "nombre": p.nombre, "precio": p.precio, "stock": p.stock} for p in productos]

# Crear un nuevo producto
@app.post("/products")
def crear_producto(producto: ProductoSchema):
    nuevo_producto = Producto(nombre=producto.nombre, precio=producto.precio, stock=producto.stock)
    session.add(nuevo_producto)
    session.commit()
    return JSONResponse(content={"mensaje": "Producto creado con éxito"}, status_code=201)

# Obtener un producto por id
@app.get("/products/{id}")
def obtener_producto(id: int):
    producto = session.query(Producto).filter(Producto.id == id).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"id": producto.id, "nombre": producto.nombre, "precio": producto.precio, "stock": producto.stock}

# Actualizar un producto
@app.put("/products/{id}")
def actualizar_producto(id: int, producto: ProductoSchema):
    producto_actual = session.query(Producto).filter(Producto.id == id).first()
    if producto_actual is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    producto_actual.nombre = producto.nombre
    producto_actual.precio = producto.precio
    producto_actual.stock = producto.stock
    session.commit()
    return JSONResponse(content={"mensaje": "Producto actualizado con éxito"}, status_code=200)

# Eliminar un producto
@app.delete("/products/{id}")
def eliminar_producto(id: int):
    producto = session.query(Producto).filter(Producto.id == id).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    session.delete(producto)
    session.commit()
    return JSONResponse(content={"mensaje": "Producto eliminado con éxito"}, status_code=200)