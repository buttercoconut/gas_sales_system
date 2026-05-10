from pydantic import BaseModel, Field
from typing import Optional

class PaymentCreate(BaseModel):
    contract_id: int = Field(..., example=1)
    amount: float = Field(..., example=50000.0)
    payment_date: str = Field(..., example="2024-05-15")
    method: str = Field(..., example="credit_card")

class PaymentRead(PaymentCreate):
    id: int
    class Config:
        orm_mode = True
