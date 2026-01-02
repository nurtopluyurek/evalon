"""Database connection for Strategy Service"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from models import Base

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Strategy service database tables created")
