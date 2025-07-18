from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import product_repository
from app.schemas.schemas import ProductCreate

def add_products(db: Session, warehouse_id: int, products: list[ProductCreate]):
    return product_repository.create_products_for_warehouse(db, warehouse_id, products)

def get_product(db: Session, product_id: int):
    product = product_repository.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
