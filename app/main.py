from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base, SessionLocal
from app.routers import products, orders
from app.seed import seed_products

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Amit iPhone Store",
    description="iPhone E-Commerce Backend",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(products.router)
app.include_router(orders.router)


@app.on_event("startup")
def seed_database():
    db = SessionLocal()
    try:
        seed_products(db)
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "Welcome to Amit iPhone Store!",
        "created_by": "Amit Navande"
    }