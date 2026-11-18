from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Product, Order
from app.schemas import OrderCreate

router = APIRouter(
    prefix="/api/orders",
    tags=["Orders"]
)


@router.post("/")
def create_order(
    data: OrderCreate,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == data.product_id
    ).first()

    if not product:
        raise HTTPException(404, "Product not found")

    if data.quantity <= 0:
        raise HTTPException(400, "Invalid quantity")

    if product.stock < data.quantity:
        raise HTTPException(400, "Out of stock")

    total = product.price * data.quantity

    order = Order(
        customer_name=data.customer_name,
        email=data.email,
        product_id=data.product_id,
        quantity=data.quantity,
        total_price=total,
        status="Pending",
        unit_price=product.price  # Include unit price
    )

    product.stock -= data.quantity

    db.add(order)
    db.commit()
    db.refresh(order)

    return {
        "message": "Order placed successfully!",
        "order_id": order.id,
        "total_price": total
    }


@router.get("/")
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()