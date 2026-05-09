from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class UsageDataCreate(BaseModel):
    contract_id: int
    usage_kwh: float
    recorded_at: str

class UsageDataOut(UsageDataCreate):
    id: int

# In-memory store for demo purposes
_usage_data = []
_next_id = 1

@router.post("/", response_model=UsageDataOut)
def create_usage(data: UsageDataCreate):
    global _next_id
    data_dict = data.dict()
    data_dict["id"] = _next_id
    _next_id += 1
    _usage_data.append(data_dict)
    return data_dict

@router.get("/", response_model=List[UsageDataOut])
def list_usage():
    return _usage_data

@router.get("/{usage_id}", response_model=UsageDataOut)
def get_usage(usage_id: int):
    for u in _usage_data:
        if u["id"] == usage_id:
            return u
    raise HTTPException(status_code=404, detail="Usage data not found")
