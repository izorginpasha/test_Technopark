from decimal import Decimal
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from db.session import AsyncSessionLocal
from db.models import CalcResult


async def create_calc_result(total_cost: Decimal) -> None:
    async with AsyncSessionLocal() as session:
        try:
            obj = CalcResult(total_cost_rub=total_cost)
            session.add(obj)
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise



