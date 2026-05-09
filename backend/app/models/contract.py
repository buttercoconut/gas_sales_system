"""Contract interface and Pydantic schemas."""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ContractBase(BaseModel):
    customer_id: int
    gas_type: str
    start_date: datetime
    end_date: Optional[datetime] = None
    status: str

class ContractCreate(ContractBase):
    pass

class ContractRead(ContractBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
