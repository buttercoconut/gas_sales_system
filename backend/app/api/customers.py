from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..models.customer import CustomerCreate, CustomerRead, CustomerUpdate
from ..services.customer_service import CustomerService
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=CustomerRead, status_code=status.HTTP_201_CREATED)
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return CustomerService.create_customer(db, customer)

@router.get("/", response_model=List[CustomerRead])
async def list_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return CustomerService.list_customers(db, skip=skip, limit=limit)

@router.get("/{customer_id}", response_model=CustomerRead)
async def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = CustomerService.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/{customer_id}", response_model=CustomerRead)
async def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    updated = CustomerService.update_customer(db, customer_id, customer)
    if not updated:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    deleted = CustomerService.delete_customer(db, customer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Customer not found")
    return None
