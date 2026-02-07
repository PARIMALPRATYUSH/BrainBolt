from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "BrainBolt API"
    DATABASE_URL: str = "postgresql+asyncpg://postgres:password@db:5432/brainbolt"
    REDIS_URL: str = "redis://redis:6379/0"
    
    class Config:
        env_file = ".env"

settings = Settings()
