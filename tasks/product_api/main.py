import fastapi
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    """
    Modelo de producto
    """
    id: int
    nombre: str
    precio: float

@app.get('/products')
def obtener_productos():
    """
    Obtiene una lista de productos
    """
    productos = [{'id': 1, 'nombre': 'Producto 1', 'precio': 10.99}, {'id': 2, 'nombre': 'Producto 2', 'precio': 5.99}]
    return productos