from pydantic import BaseModel, Field
from typing import Optional

class ContractBase(BaseModel):
    customer_id: int = Field(..., example=1)
    contract_type: str = Field(..., example="전기요금 계약")
    start_date: str = Field(..., example="2024-01-01")
    end_date: Optional[str] = Field(None, example="2024-12-31")
    status: str = Field(..., example="active")

class ContractCreate(ContractBase):
    pass

class ContractUpdate(BaseModel):
    contract_type: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    status: Optional[str]

class ContractRead(ContractBase):
    id: int
    class Config:
        orm_mode = True
