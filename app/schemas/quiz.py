from pydantic import BaseModel
from typing import List, Optional

class QuestionResponse(BaseModel):
    userId: str
    questionId: str
    difficulty: int
    prompt: str
    choices: List[str]
    choices: List[str]

class AnswerRequest(BaseModel):
    userId: str
    questionId: str
    answer: str
    idempotencyKey: str

class AnswerResponse(BaseModel):
    correct: bool
    newDifficulty: float
    newStreak: int
    scoreDelta: int
    totalScore: int
    dailyStats: dict # {attempts: int, correct: int}

class MetricsResponse(BaseModel):
    currentDifficulty: float
    streak: int
    maxStreak: int
    totalScore: int
    scoreRank: Optional[int]
    streakRank: Optional[int]
    dailyAccuracy: float
