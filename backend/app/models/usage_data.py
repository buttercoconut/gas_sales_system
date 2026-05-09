"""Usage data model and schemas."""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UsageBase(BaseModel):
    contract_id: int
    timestamp: datetime
    volume: float
    unit: str

class UsageCreate(UsageBase):
    pass

class UsageRead(UsageBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
