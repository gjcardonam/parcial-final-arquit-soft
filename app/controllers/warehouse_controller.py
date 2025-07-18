from fastapi import APIRouter, Depends, HTTPException, Request, Header
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.schemas.schemas import WarehouseCreate, WarehouseResponse, ProductCreate
from app.services import warehouse_service, product_service
from app.utils import hateoas

router = APIRouter()


@router.get("/warehouse/{warehouse_id}", response_model=WarehouseResponse, name="get_warehouse")
def get_warehouse(
    warehouse_id: int,
    request: Request,
    db: Session = Depends(get_db),
    x_api_version: str = Header(None)
):
    if x_api_version != "v1":
        raise HTTPException(status_code=400, detail="API version not supported")

    warehouse = warehouse_service.get_warehouse(db, warehouse_id)
    response = WarehouseResponse.model_validate(warehouse)
    response.links = hateoas.warehouse_links(request, warehouse.id)

    for product in response.products:
        product.links = hateoas.product_links(request, product.id)
    return response


@router.post("/warehouse/", response_model=WarehouseResponse, name="create_warehouse")
def create_warehouse(
    warehouse: WarehouseCreate,
    request: Request,
    db: Session = Depends(get_db),
    x_api_version: str = Header(None)
):
    if x_api_version != "v1":
        raise HTTPException(status_code=400, detail="API version not supported")

    new_warehouse = warehouse_service.create_warehouse(db, warehouse)
    response = WarehouseResponse.model_validate(new_warehouse)
    response.links = hateoas.warehouse_links(request, new_warehouse.id)
    return response


@router.post("/warehouse/{warehouse_id}/products", response_model=WarehouseResponse, name="add_products_to_warehouse")
def add_products_to_warehouse(
    warehouse_id: int,
    products: List[ProductCreate],
    request: Request,
    db: Session = Depends(get_db),
    x_api_version: str = Header(None)
):
    if x_api_version != "v1":
        raise HTTPException(status_code=400, detail="API version not supported")

    warehouse_service.verify_warehouse_exists(db, warehouse_id)
    product_service.add_products(db, warehouse_id, products)
    warehouse = warehouse_service.get_warehouse(db, warehouse_id)

    response = WarehouseResponse.model_validate(warehouse)
    response.links = hateoas.warehouse_links(request, warehouse.id)
    for product in response.products:
        product.links = hateoas.product_links(request, product.id)
    return response
