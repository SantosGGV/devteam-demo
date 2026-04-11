from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
API de Productos con FastAPI y SQLAlchemy

Esta API gestiona una lista de productos con nombre, precio y stock.

### Requisitos

- Python 3.8 o superior
- FastAPI
- SQLAlchemy

### Instalación

1. Clona el repositorio
2. Crea un entorno virtual con `python -m venv venv`
3. Activa el entorno virtual con `source venv/bin/activate`
4. Instala las dependencias con `pip install -r requirements.txt`
5. Corre la API con `uvicorn main:app --host 0.0.0.0 --port 8000`

### Endpoints

- GET /products: Obtiene la lista de productos
- POST /products: Crea un nuevo producto
- GET /products/{id}: Obtiene un producto por ID
- PUT /products/{id}: Actualiza un producto
- DELETE /products/{id}: Elimina un producto
"""

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URL = 'sqlite:///products.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definición de la tabla de productos
class Producto(Base):
    """
    Clase que representa un producto

    Attributes:
        id (int): ID del producto
        nombre (str): Nombre del producto
        precio (float): Precio del producto
        stock (int): Stock del producto
    """
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Float)
    stock = Column(Integer)

# Creación de la base de datos
Base.metadata.create_all(engine)

# Creación de la API
app = FastAPI()

# Ruta para obtener la lista de productos
@app.get('/products')
def obtener_productos(db: Session = Depends(get_db)) -> List[Producto]:
    """
    Obtiene la lista de productos

    Returns:
        List[Producto]: Lista de productos
    """
    return db.query(Producto).all()

# Ruta para crear un nuevo producto
@app.post('/products')
def crear_producto(db: Session = Depends(get_db), producto: ProductoCreate = Body(...)) -> Producto:
    """
    Crea un nuevo producto

    Args:
        producto (ProductoCreate): Datos del producto a crear

    Returns:
        Producto: El producto creado
    """
    db_producto = Producto(nombre=producto.nombre, precio=producto.precio, stock=producto.stock)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto
