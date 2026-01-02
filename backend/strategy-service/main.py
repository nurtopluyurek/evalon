"""
Strategy Service - Manages trading strategies
"""
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional

from config import settings
from database import get_db, init_db
from models import Strategy
from schemas import (
    StrategyCreate, StrategyUpdate, StrategyResponse, HealthResponse
)

app = FastAPI(
    title=f"Evalon {settings.SERVICE_NAME}",
    description="Trading Strategy Management Service",
    version=settings.VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_db()

# ==================== ENDPOINTS ====================

@app.get("/", tags=["Root"])
def root():
    return {
        "service": settings.SERVICE_NAME,
        "version": settings.VERSION,
        "status": "running"
    }

@app.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check(db: Session = Depends(get_db)):
    """Health check"""
    try:
        strategy_count = db.query(Strategy).count()
        return HealthResponse(
            status="healthy",
            service=settings.SERVICE_NAME,
            version=settings.VERSION,
            timestamp=datetime.utcnow()
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Service unhealthy: {str(e)}"
        )

@app.post("/strategies", response_model=StrategyResponse, tags=["Strategies"])
def create_strategy(
    strategy_data: StrategyCreate, 
    db: Session = Depends(get_db)
):
    """
    Create a new trading strategy
    
    - **name**: Strategy name
    - **description**: Strategy description
    - **rules**: Strategy rules (can be natural language or JSON)
    - **user_id**: ID of the user creating the strategy
    """
    new_strategy = Strategy(
        user_id=strategy_data.user_id,
        name=strategy_data.name,
        description=strategy_data.description,
        rules=strategy_data.rules,
        status="created"
    )
    
    db.add(new_strategy)
    db.commit()
    db.refresh(new_strategy)
    
    return new_strategy

@app.get("/strategies", response_model=List[StrategyResponse], tags=["Strategies"])
def list_strategies(
    user_id: Optional[int] = None,
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """
    List strategies with optional filters
    
    - **user_id**: Filter by user ID
    - **status**: Filter by status
    - **skip**: Number of records to skip
    - **limit**: Maximum number of records
    """
    query = db.query(Strategy)
    
    if user_id:
        query = query.filter(Strategy.user_id == user_id)
    
    if status:
        query = query.filter(Strategy.status == status)
    
    strategies = query.offset(skip).limit(limit).all()
    return strategies

@app.get("/strategies/{strategy_id}", response_model=StrategyResponse, tags=["Strategies"])
def get_strategy(strategy_id: int, db: Session = Depends(get_db)):
    """Get strategy by ID"""
    strategy = db.query(Strategy).filter(Strategy.id == strategy_id).first()
    
    if not strategy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Strategy not found"
        )
    
    return strategy

@app.put("/strategies/{strategy_id}", response_model=StrategyResponse, tags=["Strategies"])
def update_strategy(
    strategy_id: int,
    strategy_data: StrategyUpdate,
    db: Session = Depends(get_db)
):
    """Update strategy"""
    strategy = db.query(Strategy).filter(Strategy.id == strategy_id).first()
    
    if not strategy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Strategy not found"
        )
    
    # Update fields
    if strategy_data.name:
        strategy.name = strategy_data.name
    if strategy_data.description:
        strategy.description = strategy_data.description
    if strategy_data.rules:
        strategy.rules = strategy_data.rules
    if strategy_data.status:
        strategy.status = strategy_data.status
    
    strategy.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(strategy)
    
    return strategy

@app.delete("/strategies/{strategy_id}", tags=["Strategies"])
def delete_strategy(strategy_id: int, db: Session = Depends(get_db)):
    """Delete strategy"""
    strategy = db.query(Strategy).filter(Strategy.id == strategy_id).first()
    
    if not strategy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Strategy not found"
        )
    
    db.delete(strategy)
    db.commit()
    
    return {"message": "Strategy deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
