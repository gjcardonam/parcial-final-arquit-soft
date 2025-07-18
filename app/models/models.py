from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base

class Warehouse(Base):
    __tablename__ = "warehouses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    location = Column(String)
    products = relationship("Product", back_populates="warehouse")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    quantity = Column(Integer, default=0)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))
    warehouse = relationship("Warehouse", back_populates="products")
