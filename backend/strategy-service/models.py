"""Database models for Strategy Service"""
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class StrategyStatus(str, enum.Enum):
    CREATED = "created"
    BACKTESTING = "backtesting"
    PAPER_TRADING = "paper_trading"
    LIVE_TRADING = "live_trading"
    PAUSED = "paused"
    ARCHIVED = "archived"

class Strategy(Base):
    """Trading strategy model"""
    __tablename__ = "strategies"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    rules = Column(Text, nullable=False)  # JSON or plain text rules
    status = Column(String(50), default=StrategyStatus.CREATED.value)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<Strategy(id={self.id}, name={self.name}, status={self.status})>"
