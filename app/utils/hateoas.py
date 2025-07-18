from fastapi import Request

def warehouse_links(request: Request, warehouse_id: int):
    return {
        "self": str(request.url_for("get_warehouse", warehouse_id=warehouse_id)),
        "add_products": str(request.url_for("add_products_to_warehouse", warehouse_id=warehouse_id))
    }

def product_links(request: Request, product_id: int):
    return {
        "self": str(request.url_for("get_product", product_id=product_id))
    }
