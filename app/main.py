from app.routers import payments
from fastapi import FastAPI

app = FastAPI(title="EcoMarket Staging API", version="1.0.0")

# Incluimos el router de pagos
app.include_router(payments.router)


@app.get("/")
def root():
  return {"message": "EcoMarket Staging API is online", "status": "active"}