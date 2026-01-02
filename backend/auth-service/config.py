"""
Configuration settings for Auth Service
"""
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Service Info
    SERVICE_NAME: str = "auth-service"
    VERSION: str = "0.1.0"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8001
    
    # Database
    DATABASE_URL: str = "postgresql://evalon:evalon123@localhost:5432/evalon_db"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()
