## API de Productos con FastAPI y SQLAlchemy

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