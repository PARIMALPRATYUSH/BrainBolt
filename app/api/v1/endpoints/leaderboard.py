from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID

from app.core.database import get_db
from app.services.leaderboard_service import LeaderboardService

router = APIRouter()

@router.get("/score")
async def get_score_leaderboard(limit: int = 10, db: AsyncSession = Depends(get_db)):
    service = LeaderboardService(db)
    leaders = await service.get_score_leaderboard(limit)
    return leaders

@router.get("/streak")
async def get_streak_leaderboard(limit: int = 10, db: AsyncSession = Depends(get_db)):
    service = LeaderboardService(db)
    leaders = await service.get_streak_leaderboard(limit)
    return leaders
