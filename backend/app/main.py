from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import customers, contracts, usage, payments

app = FastAPI(title="Gas Sales System API", version="1.0.0")

# CORS 설정 (필요에 따라 도메인 조정)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 포함
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(contracts.router, prefix="/contracts", tags=["Contracts"])
app.include_router(usage.router, prefix="/usage", tags=["Usage"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}
