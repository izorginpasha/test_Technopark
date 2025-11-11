from datetime import datetime
from decimal import Decimal
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Numeric, TIMESTAMP, func


class Base(DeclarativeBase):
    pass

class CalcResult(Base):
    __tablename__ = "calc_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    total_cost_rub: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=False),
        server_default=func.now(),
        nullable=False,
    )

