from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError

from schemas.calc import CalcRequest, CalcResponse
from services.calc_service import calculate_total_cost

calc_router = APIRouter()


@calc_router.post("/calc", response_model=CalcResponse)
async def calc_endpoint(payload: CalcRequest):
    try:
        total = await calculate_total_cost(payload)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database error")
    return CalcResponse(total_cost_rub=total)
