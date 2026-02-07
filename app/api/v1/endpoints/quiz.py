from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import Optional

from app.core.database import get_db
from app.services.quiz_service import QuizService
from app.schemas.quiz import QuestionResponse, AnswerRequest, AnswerResponse, MetricsResponse

router = APIRouter()

@router.get("/next", response_model=QuestionResponse)
async def get_next_question(
    userId: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    service = QuizService(db)
    return await service.get_next_question(userId)

@router.post("/answer", response_model=AnswerResponse)
async def submit_answer(
    request: AnswerRequest,
    db: AsyncSession = Depends(get_db)
):
    service = QuizService(db)
    return await service.submit_answer(request)

@router.get("/metrics/{user_id}", response_model=MetricsResponse)
async def get_user_metrics(user_id: str, db: AsyncSession = Depends(get_db)):
    service = QuizService(db)
    return await service.get_user_metrics(user_id)
