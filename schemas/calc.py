from pydantic import BaseModel, Field, conlist
from typing import List
from decimal import Decimal

class Material(BaseModel):
    name: str
    qty: float = Field(..., gt=0)
    price_rub: Decimal = Field(..., gt=0)


class CalcRequest(BaseModel):
    materials: conlist(Material, min_length=1)


class CalcResponse(BaseModel):
    total_cost_rub:  Decimal
