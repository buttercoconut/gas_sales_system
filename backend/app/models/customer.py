"""Customer model definitions using Pydantic and SQLAlchemy."""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None

class CustomerCreate(CustomerBase):
    password: str

class CustomerRead(CustomerBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
