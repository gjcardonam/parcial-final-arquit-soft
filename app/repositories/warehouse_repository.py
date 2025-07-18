from sqlalchemy.orm import Session
from app.models.models import Warehouse
from app.schemas.schemas import WarehouseCreate
from sqlalchemy.exc import SQLAlchemyError

def get_warehouse_by_id(db: Session, warehouse_id: int):
    return db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()

def create_warehouse(db: Session, warehouse: WarehouseCreate):
    try:
        db_warehouse = Warehouse(name=warehouse.name, location=warehouse.location)
        db.add(db_warehouse)
        db.commit()
        db.refresh(db_warehouse)
        return db_warehouse
    except SQLAlchemyError as e:
        db.rollback()
        raise e
