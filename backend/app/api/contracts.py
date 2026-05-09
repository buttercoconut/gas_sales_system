from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ContractCreate(BaseModel):
    customer_id: int
    gas_type: str
    rate_per_unit: float
    start_date: str
    end_date: str

class ContractOut(ContractCreate):
    id: int

# In-memory store for demo purposes
_contracts = []
_next_id = 1

@router.post("/", response_model=ContractOut)
def create_contract(contract: ContractCreate):
    global _next_id
    contract_dict = contract.dict()
    contract_dict["id"] = _next_id
    _next_id += 1
    _contracts.append(contract_dict)
    return contract_dict

@router.get("/", response_model=List[ContractOut])
def list_contracts():
    return _contracts

@router.get("/{contract_id}", response_model=ContractOut)
def get_contract(contract_id: int):
    for c in _contracts:
        if c["id"] == contract_id:
            return c
    raise HTTPException(status_code=404, detail="Contract not found")
