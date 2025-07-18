from pydantic import BaseModel, Field
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    links: Optional[dict] = Field(default_factory=dict)
    model_config = {"from_attributes": True}

class WarehouseBase(BaseModel):
    name: str
    location: str

class WarehouseCreate(WarehouseBase):
    pass

class WarehouseResponse(WarehouseBase):
    id: int
    products: List[ProductResponse] = Field(default_factory=list)
    links: Optional[dict] = Field(default_factory=dict)
    model_config = {"from_attributes": True}