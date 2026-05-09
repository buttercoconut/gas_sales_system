from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str

class CustomerOut(CustomerCreate):
    id: int

# In-memory store for demo purposes
_customers = []
_next_id = 1

@router.post("/", response_model=CustomerOut)
def create_customer(customer: CustomerCreate):
    global _next_id
    customer_dict = customer.dict()
    customer_dict["id"] = _next_id
    _next_id += 1
    _customers.append(customer_dict)
    return customer_dict

@router.get("/", response_model=List[CustomerOut])
def list_customers():
    return _customers

@router.get("/{customer_id}", response_model=CustomerOut)
def get_customer(customer_id: int):
    for c in _customers:
        if c["id"] == customer_id:
            return c
    raise HTTPException(status_code=404, detail="Customer not found")
