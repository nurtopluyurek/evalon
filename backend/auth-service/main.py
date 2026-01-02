"""
Main FastAPI application for Auth Service
Handles user authentication and authorization
"""
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime
from typing import List

from config import settings
from database import get_db, init_db
from models import User
from schemas import (
    UserCreate, UserResponse, UserLogin, 
    Token, HealthResponse
)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Initialize FastAPI app
app = FastAPI(
    title=f"Evalon {settings.SERVICE_NAME}",
    description="Authentication and Authorization Service",
    version=settings.VERSION
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    init_db()

# ==================== UTILITY FUNCTIONS ====================

def hash_password(password: str) -> str:
    """Hash a password"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against hash"""
    return pwd_context.verify(plain_password, hashed_password)

# ==================== ENDPOINTS ====================

@app.get("/", tags=["Root"])
def root():
    """Root endpoint"""
    return {
        "service": settings.SERVICE_NAME,
        "version": settings.VERSION,
        "status": "running",
        "docs": "/docs"
    }

@app.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check(db: Session = Depends(get_db)):
    """Health check endpoint"""
    try:
        # Check database connection
        user_count = db.query(User).count()
        
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

@app.post("/register", response_model=UserResponse, tags=["Authentication"])
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user
    
    - **email**: User's email (must be unique)
    - **password**: User's password (will be hashed)
    - **full_name**: User's full name
    """
    # Check if user exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    new_user = User(
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        full_name=user_data.full_name
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@app.post("/login", response_model=Token, tags=["Authentication"])
def login_user(credentials: UserLogin, db: Session = Depends(get_db)):
    """
    Login user and return access token
    
    - **email**: User's email
    - **password**: User's password
    """
    # Find user
    user = db.query(User).filter(User.email == credentials.email).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    # Verify password
    if not verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    # Check if user is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is disabled"
        )
    
    # For now, return a simple token (user_id)
    # TODO: Implement proper JWT token generation
    return Token(
        access_token=f"user_{user.id}_token",
        token_type="bearer"
    )

@app.get("/users", response_model=List[UserResponse], tags=["Users"])
def list_users(
    skip: int = 0, 
    limit: int = 10, 
    db: Session = Depends(get_db)
):
    """
    List all users (for development purposes)
    
    - **skip**: Number of records to skip
    - **limit**: Maximum number of records to return
    """
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@app.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get user by ID"""
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user

# ==================== MAIN ====================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
