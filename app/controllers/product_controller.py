from fastapi import APIRouter, Depends, HTTPException, Request, Header
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.schemas import ProductResponse
from app.services import product_service
from app.utils import hateoas

router = APIRouter()


@router.get("/product/{product_id}", response_model=ProductResponse, name="get_product")
def get_product(
    product_id: int,
    request: Request,
    db: Session = Depends(get_db),
    x_api_version: str = Header(None)
):
    if x_api_version != "v1":
        raise HTTPException(status_code=400, detail="API version not supported")

    product = product_service.get_product(db, product_id)
    response = ProductResponse.model_validate(product)
    response.links = hateoas.product_links(request, product.id)
    return response
