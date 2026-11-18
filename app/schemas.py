from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    name: str
    price: float
    description: str = ""
    image_url: str = ""
    stock: int = 10


class ProductResponse(ProductCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class OrderCreate(BaseModel):
    customer_name: str
    email: str
    product_id: int
    quantity: int