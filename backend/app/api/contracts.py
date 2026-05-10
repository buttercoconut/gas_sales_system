from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..models.contract import ContractCreate, ContractRead, ContractUpdate
from ..services.contract_service import ContractService
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=ContractRead, status_code=status.HTTP_201_CREATED)
async def create_contract(contract: ContractCreate, db: Session = Depends(get_db)):
    return ContractService.create_contract(db, contract)

@router.get("/", response_model=List[ContractRead])
async def list_contracts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ContractService.list_contracts(db, skip=skip, limit=limit)

@router.get("/{contract_id}", response_model=ContractRead)
async def get_contract(contract_id: int, db: Session = Depends(get_db)):
    contract = ContractService.get_contract(db, contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    return contract

@router.put("/{contract_id}", response_model=ContractRead)
async def update_contract(contract_id: int, contract: ContractUpdate, db: Session = Depends(get_db)):
    updated = ContractService.update_contract(db, contract_id, contract)
    if not updated:
        raise HTTPException(status_code=404, detail="Contract not found")
    return updated

@router.delete("/{contract_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contract(contract_id: int, db: Session = Depends(get_db)):
    deleted = ContractService.delete_contract(db, contract_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contract not found")
    return None
