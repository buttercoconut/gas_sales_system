from pydantic import BaseModel, Field
from typing import Optional

class UsageCreate(BaseModel):
    contract_id: int = Field(..., example=1)
    usage_date: str = Field(..., example="2024-05-01")
    volume: float = Field(..., example=120.5)
    unit: str = Field(..., example="kWh")

class UsageRead(UsageCreate):
    id: int
    class Config:
        orm_mode = True
