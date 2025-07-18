from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import warehouse_repository
from app.schemas.schemas import WarehouseCreate

def get_warehouse(db: Session, warehouse_id: int):
    warehouse = warehouse_repository.get_warehouse_by_id(db, warehouse_id)
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return warehouse

def create_warehouse(db: Session, warehouse: WarehouseCreate):
    return warehouse_repository.create_warehouse(db, warehouse)

def verify_warehouse_exists(db: Session, warehouse_id: int):
    if not warehouse_repository.get_warehouse_by_id(db, warehouse_id):
        raise HTTPException(status_code=404, detail="Warehouse not found")
