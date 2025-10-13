from fastapi import APIRouter, Depends, status, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.database import get_db, engine
import app.core.model as model
from typing import Annotated, List
from sqlalchemy.orm import Session
from app.core import model, schemas
from app.core.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from datetime import timedelta

router = APIRouter(prefix="/users")
model.Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

# Helper function to check if user has management role
def check_management_role(current_user: dict):
    if current_user.get("role") != "Management":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Operation requires Management role"
        )

@router.get("/", response_model=List[schemas.UserResponse], status_code=status.HTTP_200_OK)
async def get_all_users(
    db: db_dependency,
    current_user: dict = Security(get_current_user)
):
    """Get all users (Management role required)"""
    check_management_role(current_user)
    
    users = db.query(model.Users).all()
    return users

@router.get("/{user_id}", response_model=schemas.UserResponse, status_code=status.HTTP_200_OK)
async def get_user(
    user_id: str,
    db: db_dependency,
    current_user: dict = Security(get_current_user)
):
    """Get user details (Management or self only)"""
    # Allow access if user is Management or accessing their own data
    if current_user.get("role") != "Management" and current_user.get("user_id") != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this user's data"
        )
    
    user = db.query(model.Users).filter(model.Users.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    return user

@router.post("/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: schemas.UserCreate,
    db: db_dependency,
    current_user: dict = Security(get_current_user)
):
    """Create new user (Management role required)"""
    check_management_role(current_user)
    
    # Check if username already exists
    existing_user = db.query(model.Users).filter(model.Users.user_name == user.user_name).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    
    # Hash the password
    hashed_password = get_password_hash(user.password)
    
    # Create new user
    new_user = model.Users(
        user_name=user.user_name,
        password_hash=hashed_password,
        role=user.role
    )
    
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/{user_id}", response_model=schemas.UserResponse, status_code=status.HTTP_200_OK)
async def update_user(
    user_id: str,
    user_update: schemas.UserUpdate,
    db: db_dependency,
    current_user: dict = Security(get_current_user)
):
    """Update user details (Management or self only)"""
    # Check if user exists
    user = db.query(model.Users).filter(model.Users.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    # Allow access if user is Management or updating their own data
    if current_user.get("role") != "Management" and current_user.get("user_id") != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this user"
        )
    
    # Only Management can update roles
    if user_update.role and current_user.get("role") != "Management":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Management can update user roles"
        )
    
    try:
        # Update username if provided
        if user_update.user_name:
            existing_user = db.query(model.Users).filter(
                model.Users.user_name == user_update.user_name,
                model.Users.user_id != user_id
            ).first()
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Username already exists"
                )
            user.user_name = user_update.user_name
        
        # Update password if provided
        if user_update.password:
            user.password_hash = get_password_hash(user_update.password)
        
        # Update role if provided (Management only)
        if user_update.role:
            user.role = user_update.role
        
        db.commit()
        db.refresh(user)
        return user
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(
    user_id: str,
    db: db_dependency,
    current_user: dict = Security(get_current_user)
):
    """Delete user (Management role required)"""
    check_management_role(current_user)
    
    # Check if user exists
    user = db.query(model.Users).filter(model.Users.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    try:
        db.delete(user)
        db.commit()
        return {"detail": f"User {user_id} deleted successfully"}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/login")
async def login(
    db: db_dependency,
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """Authenticate user and return JWT token"""
    # Find user by username
    user = db.query(model.Users).filter(model.Users.user_name == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verify password
    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.user_id, "role": user.role},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.user_id,
        "username": user.user_name,
        "role": user.role
    }

