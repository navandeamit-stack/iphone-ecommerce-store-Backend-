# Amit iPhone Store Backend

A beginner-friendly FastAPI backend for the React iPhone e-commerce frontend.

## Requirements
- Python 3.10+
- VS Code

## 1. Open this folder in VS Code
Open the `iphone-store-backend` folder (the folder containing `requirements.txt`).

## 2. Create and activate a virtual environment

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:
```powershell
py -m venv .venv
.venv\\Scripts\\Activate.ps1
```

## 3. Install packages
```bash
pip install -r requirements.txt
```

## 4. Start the backend
```bash
uvicorn app.main:app --reload
```

Open:
- Backend home: http://127.0.0.1:8000/
- Interactive API documentation: http://127.0.0.1:8000/docs

The SQLite database file `iphone_store.db` is created automatically on first run.
The first run also inserts sample products named iPhone 1 through iPhone 18. Prices and descriptions are sample data; edit them through the API or in `app/seed.py`.

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check backend |
| GET | `/api/products/` | List products |
| GET | `/api/products/{product_id}` | Get one product |
| POST | `/api/products/` | Add a product |
| PUT | `/api/products/{product_id}` | Update a product |
| DELETE | `/api/products/{product_id}` | Delete a product |
| POST | `/api/orders/` | Place an order |
| GET | `/api/orders/` | List orders |
| GET | `/api/orders/{order_id}` | Get one order |

## Test a product
In `/docs`, open `POST /api/products/` and use:
```json
{
  "name": "iPhone 18 Pro",
  "price": 149999,
  "description": "Sample product description",
  "image_url": "",
  "stock": 10
}
```

## Test an order
Use a real product ID returned by `GET /api/products/`:
```json
{
  "customer_name": "Amit Navande",
  "email": "amit@example.com",
  "product_id": 1,
  "quantity": 1
}
```

## Connect React to this backend
The backend allows local React development origins:
- http://localhost:3000 (Next.js)
- http://localhost:5173 (Vite)
- http://localhost:3001

Example:
```js
const response = await fetch("http://127.0.0.1:8000/api/products/");
const products = await response.json();
```

Important: this is a learning/demo backend. Before real customers use it, add authentication and admin authorization, payment-gateway verification, HTTPS, production database configuration, rate limiting, and stronger order/customer data protections. Never store card numbers or CVV in this app.
