"""Configuration for Strategy Service"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SERVICE_NAME: str = "strategy-service"
    VERSION: str = "0.1.0"
    HOST: str = "0.0.0.0"
    PORT: int = 8002
    DATABASE_URL: str = "postgresql://evalon:evalon123@localhost:5432/evalon_db"
    
    class Config:
        env_file = ".env"

settings = Settings()
