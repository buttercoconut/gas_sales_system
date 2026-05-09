"""Payment model and schemas."""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PaymentBase(BaseModel):
    customer_id: int
    amount: float
    method: str
    status: str
    timestamp: datetime

class PaymentCreate(PaymentBase):
    pass

class PaymentRead(PaymentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
