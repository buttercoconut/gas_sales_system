# Service for usage data and billing calculations
from typing import List
from ..models import UsageData, Contract

# In-memory store for demo purposes
_usage_data: List[UsageData] = []
_next_id = 1

# Simple billing: cost = usage_kwh * rate_per_unit

def create_usage(contract_id: int, usage_kwh: float, recorded_at: str) -> UsageData:
    global _next_id
    usage = UsageData(id=_next_id, contract_id=contract_id, usage_kwh=usage_kwh, recorded_at=recorded_at)
    _next_id += 1
    _usage_data.append(usage)
    return usage

def list_usage() -> List[UsageData]:
    return _usage_data

def get_usage(usage_id: int) -> UsageData:
    for u in _usage_data:
        if u.id == usage_id:
            return u
    raise ValueError("Usage data not found")

# Billing calculation

def calculate_bill(contract: Contract, usage: UsageData) -> float:
    return usage.usage_kwh * contract.rate_per_unit
