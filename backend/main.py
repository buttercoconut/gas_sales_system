"""FastAPI application entry point for Gas Sales System."""

from fastapi import FastAPI
from app.api import contracts, customers, usage, payments

app = FastAPI(title="Gas Sales System API")

# Include routers
app.include_router(contracts.router, prefix="/contracts", tags=["contracts"])
app.include_router(customers.router, prefix="/customers", tags=["customers"])
app.include_router(usage.router, prefix="/usage", tags=["usage"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])

@app.get("/", tags=["health"])
async def read_root():
    return {"message": "Gas Sales System API is running."}
