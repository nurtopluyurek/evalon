"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    """Schema for user registration"""
    password: str

class UserLogin(BaseModel):
    """Schema for user login"""
    email: EmailStr
    password: str

class UserResponse(UserBase):
    """Schema for user response (no password)"""
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    """Schema for authentication token"""
    access_token: str
    token_type: str = "bearer"

class HealthResponse(BaseModel):
    """Schema for health check"""
    status: str
    service: str
    version: str
    timestamp: datetime
