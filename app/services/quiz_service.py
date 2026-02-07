from datetime import datetime, timezone, timedelta
from uuid import uuid4
import random
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import structlog
from typing import Optional, List

from app.models.user import User, UserState, UserSubmission
from app.data.questions import question_repo, Question
from app.schemas.quiz import QuestionResponse, AnswerRequest, AnswerResponse, MetricsResponse
from app.core.redis import get_redis_client

logger = structlog.get_logger()

class QuizService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_or_create_user(self, user_id: Optional[str] = None) -> User:
        if user_id:
            result = await self.db.execute(select(User).where(User.id == user_id))
            user = result.scalars().first()
            if user:
                return user
        
        # Create new user if not found or no ID provided
        # Use provided ID if available, else generate new UUID string
        new_id = user_id if user_id else str(uuid4())
        new_user = User(id=new_id)
        self.db.add(new_user)
        # Initialize state
        new_state = UserState(user_id=new_user.id)
        self.db.add(new_state)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user

    async def get_user_state(self, user_id: str) -> UserState:
        result = await self.db.execute(select(UserState).where(UserState.user_id == user_id))
        state = result.scalars().first()
        if not state:
            raise HTTPException(status_code=404, detail="User state not found")
        return state

    async def check_streak_decay(self, state: UserState):
        """Halve streak if more than 24 hours since last update."""
        if not state.updated_at:
            return

        # Use UTC for consistency
        now = datetime.now(timezone.utc)
        # Ensure updated_at is timezone-aware if not already
        last_update = state.updated_at
        if last_update.tzinfo is None:
            last_update = last_update.replace(tzinfo=timezone.utc)
            
        hours_diff = (now - last_update).total_seconds() / 3600
        if hours_diff >= 24:
            logger.info("Applying streak decay", user_id=str(state.user_id), old_streak=state.current_streak)
            state.current_streak = int(state.current_streak / 2)

    async def get_next_question(self, user_id: Optional[str]) -> QuestionResponse:
        user = await self.get_or_create_user(user_id)
        state = await self.get_user_state(user.id)
        
        # Determine difficulty
        # User floor(current_difficulty) to get question
        current_diff = int(state.current_difficulty)
        
        # Fetch question pool
        pool = question_repo.get_questions_by_difficulty(current_diff)
        if not pool:
            pool = question_repo.get_all_questions()
        
        # Filter out already submitted questions
        result = await self.db.execute(select(UserSubmission.question_id).where(UserSubmission.user_id == user.id))
        answered_ids = set(result.scalars().all())
        
        available_pool = [q for q in pool if q.id not in answered_ids]
        
        if not available_pool:
            # If no questions at current difficulty, try all questions
            all_questions = question_repo.get_all_questions()
            available_pool = [q for q in all_questions if q.id not in answered_ids]

        if not available_pool:
             # Logic if ALL questions answered? 
             # Maybe reset or allow re-answering? 
             # For infinite quiz, we ideally have infinite questions.
             # MVP: If exhausted, maybe just pick random from all?
             available_pool = question_repo.get_all_questions()

        # Select random question from pool
        question = random.choice(available_pool)
        
        # Update state with this being the "current" question
        state.last_question_id = question.id
        await self.db.commit()
        await self.db.refresh(state)
        
        return QuestionResponse(
            userId=user.id,
            questionId=question.id,
            difficulty=question.difficulty,
            prompt=question.prompt,
            choices=question.choices
        )

    async def submit_answer(self, request: AnswerRequest) -> AnswerResponse:
        # Check Idempotency using Redis
        redis_client = get_redis_client()
        key = f"idempotency:{request.idempotencyKey}"
        # Set key if not exists, with 24h expiry
        is_new = await redis_client.set(key, "1", ex=86400, nx=True)
        
        if not is_new:
            # Key already exists, reject duplicate
            raise HTTPException(status_code=409, detail="Request already processed (Idempotency Key)")

        state = await self.get_user_state(request.userId)
        question = question_repo.get_question_by_id(request.questionId)
        
        if not question:
            raise HTTPException(status_code=400, detail="Invalid question ID")

        # Check streak decay
        await self.check_streak_decay(state)
            
        # Check if already answered using composite index
        result = await self.db.execute(
            select(UserSubmission).where(
                UserSubmission.user_id == request.userId, 
                UserSubmission.question_id == request.questionId
            )
        )
        if result.scalars().first():
            raise HTTPException(status_code=400, detail="Question already answered")
        
        # Check if already answered - Logic moved to DB constraint handling below
        now = datetime.now(timezone.utc)
        
        # Handle timezone awareness for last_activity_date
        last_active = state.last_activity_date
        if last_active and last_active.tzinfo is None:
            last_active = last_active.replace(tzinfo=timezone.utc)

        if last_active and last_active.date() < now.date():
             state.daily_attempts = 0
             state.daily_correct = 0

        # Update attempts
        state.daily_attempts += 1
        
        # Verify Answer
        is_correct = (request.answer.lower().strip() == question.correct_answer.lower().strip())
        
        score_delta = 0
        if is_correct:
            state.daily_correct += 1
            # Calculate Score
            daily_acc = state.daily_correct / state.daily_attempts
            
            # Streak Multiplier
            streak_mult = min(1 + (state.current_streak * 0.1), 2.5)
            
            # Accuracy Multiplier Map
            # Ranges: 0-0.2, 0.21-0.5, 0.51-0.75, 0.75-1
            # Using concrete values for these ranges to normalize score impact
            if daily_acc <= 0.2:
                acc_mult = 0.5
            elif daily_acc <= 0.5:
                acc_mult = 0.75
            elif daily_acc <= 0.75:
                acc_mult = 0.9
            else:
                acc_mult = 1.0
            
            base_score = 10
            score_delta = int(base_score * question.difficulty * streak_mult * acc_mult)
            
            state.total_score += score_delta
            state.current_streak += 1
            state.max_streak = max(state.max_streak, state.current_streak)
            
            # Increase difficulty
            # New Formula: (1 / floor(current_difficulty))
            # Use max(1.0, ...) to avoid division by zero
            current_diff = float(state.current_difficulty) if state.current_difficulty > 0 else 1.0
            increment = (1.0 / int(current_diff))
            state.current_difficulty = min(current_diff + increment, 10.0)
            
        else:
            # Wrong answer
            # Penalty based on accuracy
            daily_acc = state.daily_correct / state.daily_attempts if state.daily_attempts > 0 else 0.0
            
            # Accuracy Multiplier Map for Penalty (mirroring the gain logic or keeping it simple?)
            # The user didn't specify changing the penalty logic, only the difficulty decrement.
            # Keeping penalty logic as is: int((1 - daily_acc) * 20)
            penalty = int((1 - daily_acc) * 20)
            
            score_delta = -penalty
            state.total_score = max(0, state.total_score - penalty)
            
            state.current_streak = 0
            
            # Decrease difficulty: current - (1 / floor(current))
            current_diff = float(state.current_difficulty) if state.current_difficulty > 0 else 1.0
            decrement = 1.0 / int(current_diff)
            state.current_difficulty = max(current_diff - decrement, 1.0)

        state.last_activity_date = now
        
        # Record submission
        new_submission = UserSubmission(
            user_id=state.user_id,
            question_id=question.id,
            submitted_answer=request.answer,
            is_correct=is_correct,
            created_at=now
        )
        self.db.add(new_submission)

        try:
            # Check constraints first without finalizing
            await self.db.flush()
            
            # Update Redis Leaderboards - Fail the request if Redis is down (Strict requirement)
            redis_client = get_redis_client()
            await redis_client.zadd("leaderboard:score", {str(request.userId): state.total_score})
            # Use current_streak to reflect immediate state (reset to 0 on wrong answer)
            await redis_client.zadd("leaderboard:streak", {str(request.userId): state.current_streak})

            # Commit DB changes if Redis succeeded
            await self.db.commit()
            await self.db.refresh(state)

        except IntegrityError:
            await self.db.rollback()
            raise HTTPException(status_code=400, detail="Question already answered")
        except Exception as e:
            await self.db.rollback()
            logger.error("Transaction failed", error=str(e))
            raise HTTPException(status_code=500, detail="Internal Server Error")

        return AnswerResponse(
            correct=is_correct,
            newDifficulty=state.current_difficulty,
            newStreak=state.current_streak,
            scoreDelta=score_delta,
            totalScore=state.total_score,
            dailyStats={"attempts": state.daily_attempts, "correct": state.daily_correct}
        )

    async def get_user_metrics(self, user_id: str) -> MetricsResponse:
        state = await self.get_user_state(user_id)
        
        daily_acc = 0.0
        if state.daily_attempts > 0:
            daily_acc = state.daily_correct / state.daily_attempts
            
        # Get ranks from Redis (0-based index, so +1 for human rank)
        redis_client = get_redis_client()
        score_rank = await redis_client.zrevrank("leaderboard:score", str(user_id))
        streak_rank = await redis_client.zrevrank("leaderboard:streak", str(user_id))
        
        return MetricsResponse(
            currentDifficulty=state.current_difficulty,
            streak=state.current_streak,
            maxStreak=state.max_streak,
            totalScore=state.total_score,
            scoreRank=score_rank + 1 if score_rank is not None else None,
            streakRank=streak_rank + 1 if streak_rank is not None else None,
            dailyAccuracy=daily_acc
        )
