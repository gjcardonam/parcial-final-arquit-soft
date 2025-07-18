from fastapi import FastAPI
from app.config.database import init_db
from app.controllers import warehouse_controller, product_controller

# Crear la aplicación FastAPI
app = FastAPI(
    title="Inventory API",
    description="API RESTful para gestionar almacenes y productos con HATEOAS y versionamiento",
    version="1.0.0"
)

# Inicializar BD y crear tablas si no existen
init_db()

# Incluir routers
app.include_router(warehouse_controller.router, tags=["Warehouses"])
app.include_router(product_controller.router, tags=["Products"])

# Endpoint raíz
@app.get("/")
def root():
    return {"message": "Inventory API is running", "docs_url": "/docs"}
