from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Dict

from app.models.user import UserState
from app.schemas.quiz import MetricsResponse
from app.core.redis import get_redis_client

class LeaderboardService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.redis = get_redis_client()

    async def get_score_leaderboard(self, limit: int = 10) -> List[Dict]:
        """Fetch top N users by score from Redis ZSET."""
        # ZREVRANGE key 0 limit-1 WITHSCORES
        data = await self.redis.zrevrange("leaderboard:score", 0, limit - 1, withscores=True)
        # data is list of (member, score) tuples. member is userId
        return [{"userId": member, "score": int(score)} for member, score in data]

    async def get_streak_leaderboard(self, limit: int = 10) -> List[Dict]:
        """Fetch top N users by streak from Redis ZSET."""
        data = await self.redis.zrevrange("leaderboard:streak", 0, limit - 1, withscores=True)
        return [{"userId": member, "maxStreak": int(score)} for member, score in data]
