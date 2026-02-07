import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger, JSON, Boolean, Index, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    
    # Relationship to state
    state = relationship("UserState", back_populates="user", uselist=False, cascade="all, delete-orphan")

class UserState(Base):
    __tablename__ = "user_state"

    user_id = Column(String, ForeignKey("users.id"), primary_key=True)
    current_difficulty = Column(Float, default=1.0)
    current_streak = Column(Integer, default=0)
    max_streak = Column(Integer, default=0)
    total_score = Column(BigInteger, default=0)
    last_question_id = Column(String, nullable=True)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    # Daily tracking for accuracy
    daily_attempts = Column(Integer, default=0)
    daily_correct = Column(Integer, default=0)
    last_activity_date = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)) # For daily reset check

    __table_args__ = (
        Index('idx_user_state_updated_at', updated_at),
    )

    user = relationship("User", back_populates="state")

class UserSubmission(Base):
    __tablename__ = "user_submissions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    question_id = Column(String, nullable=False)
    submitted_answer = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        Index('idx_user_question', user_id, question_id, unique=True),
    )

    user = relationship("User", back_populates="submissions")

User.submissions = relationship("UserSubmission", back_populates="user", cascade="all, delete-orphan")
