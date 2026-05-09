from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class PaymentCreate(BaseModel):
    contract_id: int
    amount: float
    paid_at: str

class PaymentOut(PaymentCreate):
    id: int

# In-memory store for demo purposes
_payments = []
_next_id = 1

@router.post("/", response_model=PaymentOut)
def create_payment(payment: PaymentCreate):
    global _next_id
    payment_dict = payment.dict()
    payment_dict["id"] = _next_id
    _next_id += 1
    _payments.append(payment_dict)
    return payment_dict

@router.get("/", response_model=List[PaymentOut])
def list_payments():
    return _payments

@router.get("/{payment_id}", response_model=PaymentOut)
def get_payment(payment_id: int):
    for p in _payments:
        if p["id"] == payment_id:
            return p
    raise HTTPException(status_code=404, detail="Payment not found")
