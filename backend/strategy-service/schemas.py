"""Pydantic schemas for Strategy Service"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class StrategyBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    rules: str = Field(..., min_length=1)

class StrategyCreate(StrategyBase):
    """Schema for creating a strategy"""
    user_id: int

class StrategyUpdate(BaseModel):
    """Schema for updating a strategy"""
    name: Optional[str] = None
    description: Optional[str] = None
    rules: Optional[str] = None
    status: Optional[str] = None

class StrategyResponse(StrategyBase):
    """Schema for strategy response"""
    id: int
    user_id: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    timestamp: datetime
