from sqlalchemy.orm import Session
from app.models.models import Product
from app.schemas.schemas import ProductCreate
from sqlalchemy.exc import SQLAlchemyError

def create_products_for_warehouse(db: Session, warehouse_id: int, products: list[ProductCreate]):
    try:
        for prod in products:
            # Buscar si ya existe un producto con el mismo nombre y descripción en el almacén
            existing_product = (
                db.query(Product)
                .filter(
                    Product.warehouse_id == warehouse_id,
                    Product.name == prod.name,
                    Product.description == prod.description
                )
                .first()
            )

            if existing_product:
                # Si existe, sumamos la cantidad
                existing_product.quantity += prod.quantity
            else:
                # Si no existe, creamos un nuevo producto
                db_product = Product(
                    name=prod.name,
                    description=prod.description,
                    quantity=prod.quantity,
                    warehouse_id=warehouse_id
                )
                db.add(db_product)

        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()
