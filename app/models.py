from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(500))
    image_url = Column(String(500))
    stock = Column(Integer, default=10)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100))
    email = Column(String(100))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    total_price = Column(Float)
    unit_price = Column(Float, nullable=False)  # Add unit price column
    status = Column(String(50), default="Pending")