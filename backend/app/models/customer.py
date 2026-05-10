from pydantic import BaseModel, Field
from typing import Optional

class CustomerBase(BaseModel):
    name: str = Field(..., example="홍길동")
    email: str = Field(..., example="hong@example.com")
    phone: Optional[str] = Field(None, example="010-1234-5678")
    address: Optional[str] = Field(None, example="서울특별시 강남구")

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]

class CustomerRead(CustomerBase):
    id: int
    class Config:
        orm_mode = True
