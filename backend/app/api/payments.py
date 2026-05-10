from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..models.payment import PaymentCreate, PaymentRead
from ..services.payment_service import PaymentService
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=PaymentRead, status_code=status.HTTP_201_CREATED)
async def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return PaymentService.create_payment(db, payment)

@router.get("/", response_model=List[PaymentRead])
async def list_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return PaymentService.list_payments(db, skip=skip, limit=limit)

@router.get("/{payment_id}", response_model=PaymentRead)
async def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = PaymentService.get_payment(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment
