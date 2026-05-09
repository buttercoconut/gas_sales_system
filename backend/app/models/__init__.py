from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    name: str
    email: str
    phone: str

class Contract(BaseModel):
    id: int
    customer_id: int
    gas_type: str
    rate_per_unit: float
    start_date: str
    end_date: str

class UsageData(BaseModel):
    id: int
    contract_id: int
    usage_kwh: float
    recorded_at: str

class Payment(BaseModel):
    id: int
    contract_id: int
    amount: float
    paid_at: str
