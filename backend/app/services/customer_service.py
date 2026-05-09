# Service for customer-related operations
from typing import List
from ..models import Customer

# In-memory store for demo purposes
_customers: List[Customer] = []
_next_id = 1

def create_customer(name: str, email: str, phone: str) -> Customer:
    global _next_id
    customer = Customer(id=_next_id, name=name, email=email, phone=phone)
    _next_id += 1
    _customers.append(customer)
    return customer

def list_customers() -> List[Customer]:
    return _customers

def get_customer(customer_id: int) -> Customer:
    for c in _customers:
        if c.id == customer_id:
            return c
    raise ValueError("Customer not found")
