# Service for payment processing
from typing import List
from ..models import Payment

# In-memory store for demo purposes
_payments: List[Payment] = []
_next_id = 1

def create_payment(contract_id: int, amount: float, paid_at: str) -> Payment:
    global _next_id
    payment = Payment(id=_next_id, contract_id=contract_id, amount=amount, paid_at=paid_at)
    _next_id += 1
    _payments.append(payment)
    return payment

def list_payments() -> List[Payment]:
    return _payments

def get_payment(payment_id: int) -> Payment:
    for p in _payments:
        if p.id == payment_id:
            return p
    raise ValueError("Payment not found")
