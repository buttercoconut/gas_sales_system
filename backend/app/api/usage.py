from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..models.usage_data import UsageCreate, UsageRead
from ..services.usage_service import UsageService
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=UsageRead, status_code=status.HTTP_201_CREATED)
async def record_usage(usage: UsageCreate, db: Session = Depends(get_db)):
    return UsageService.record_usage(db, usage)

@router.get("/", response_model=List[UsageRead])
async def list_usages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return UsageService.list_usages(db, skip=skip, limit=limit)

@router.get("/{usage_id}", response_model=UsageRead)
async def get_usage(usage_id: int, db: Session = Depends(get_db)):
    usage = UsageService.get_usage(db, usage_id)
    if not usage:
        raise HTTPException(status_code=404, detail="Usage data not found")
    return usage
