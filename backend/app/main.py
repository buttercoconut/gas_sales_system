from fastapi import FastAPI
from .api import contracts, customers, usage, payments

app = FastAPI(title="Gas Sales System API")

app.include_router(contracts.router, prefix="/contracts", tags=["contracts"])
app.include_router(customers.router, prefix="/customers", tags=["customers"])
app.include_router(usage.router, prefix="/usage", tags=["usage"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)