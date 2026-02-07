from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import engine, Base
import structlog

logger = structlog.get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="BrainBolt API", lifespan=lifespan)

from app.api.v1.endpoints import quiz, leaderboard
app.include_router(quiz.router, prefix="/v1/quiz", tags=["quiz"])
app.include_router(leaderboard.router, prefix="/v1/leaderboard", tags=["leaderboard"])

@app.get("/")
async def root():
    logger.info("Health check endpoint called")
    return {"message": "BrainBolt Quiz Service is live"}
