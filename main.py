import logging
from fastapi import FastAPI
from api.calc import calc_router
from db.session import engine
from db.models import Base

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger("calc-service")

app = FastAPI(title="Calc Service")


@app.on_event("startup")
async def on_startup():
    #  (для тестового так как нет Alembic)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Startup complete, tables ensured.")


app.include_router(calc_router)
