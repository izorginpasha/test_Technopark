from decimal import Decimal
from schemas.calc import CalcRequest
from CRUD.calc import create_calc_result


async def calculate_total_cost(request: CalcRequest) -> Decimal:
    total = sum(
        Decimal(str(m.qty)) * Decimal(str(m.price_rub))
        for m in request.materials
    )
    await create_calc_result(total)
    return total
