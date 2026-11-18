from sqlalchemy.orm import Session
from app.models import Product

SAMPLE_PRODUCTS = [
    {
        "name": f"iPhone {number}",
        "price": 49999 + (number * 5000),
        "description": f"Sample catalogue entry for iPhone {number}.",
        "image_url": "",
        "stock": 10
    }
    for number in range(1, 19)
]


def seed_products(db: Session):
    if db.query(Product).count() == 0:
        db.add_all([Product(**item) for item in SAMPLE_PRODUCTS])
        db.commit()
