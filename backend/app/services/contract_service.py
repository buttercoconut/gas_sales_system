# Service for contract-related operations
from typing import List
from ..models import Contract

# In-memory store for demo purposes
_contracts: List[Contract] = []
_next_id = 1

def create_contract(customer_id: int, gas_type: str, rate_per_unit: float, start_date: str, end_date: str) -> Contract:
    global _next_id
    contract = Contract(id=_next_id, customer_id=customer_id, gas_type=gas_type, rate_per_unit=rate_per_unit, start_date=start_date, end_date=end_date)
    _next_id += 1
    _contracts.append(contract)
    return contract

def list_contracts() -> List[Contract]:
    return _contracts

def get_contract(contract_id: int) -> Contract:
    for c in _contracts:
        if c.id == contract_id:
            return c
    raise ValueError("Contract not found")
