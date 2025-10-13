from fastapi import APIRouter, Depends, HTTPException, status, Security
from sqlalchemy.orm import Session
from typing import Annotated, List
from app.core.database import get_db
from app.core import model, schemas
from app.core.security import get_current_user

router = APIRouter(prefix="/assistants")
db_dependency = Annotated[Session, Depends(get_db)]

def check_management_role(current_user: dict):
    if current_user.get("role") != "Management":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Management can perform this operation"
        )

@router.get("/", response_model=List[schemas.AssistantResponse], status_code=status.HTTP_200_OK)
async def get_all_assistants(
    db: db_dependency,
    current_user: dict = Security(get_current_user)
):
    """Get all assistants (Management role required)"""
    check_management_role(current_user)
    
    assistants = db.query(model.Assistants).all()
    return assistants

@router.get("/{assistant_id}", response_model=schemas.AssistantResponse, status_code=status.HTTP_200_OK)
async def get_assistant(
    assistant_id: str,
    db: db_dependency,
    current_user: dict = Security(get_current_user)
):
    """Get details of a specific assistant"""
    # Allow access if user is Management or is the assistant themselves
    if current_user.get("role") != "Management" and current_user.get("user_id") != assistant_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this assistant's data"
        )
    
    assistant = db.query(model.Assistants).filter(model.Assistants.assistant_id == assistant_id).first()
    if not assistant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Assistant with ID {assistant_id} not found"
        )
    
    return assistant

@router.post("/", response_model=schemas.AssistantResponse, status_code=status.HTTP_201_CREATED)
async def create_assistant(
    assistant: schemas.AssistantCreate,
    db: db_dependency,
    current_user: dict = Security(get_current_user)
):
    """Create a new assistant (Management role required)"""
    check_management_role(current_user)
    
    # Check if user exists and has Assistant role
    user = db.query(model.Users).filter(model.Users.user_id == assistant.user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {assistant.user_id} not found"
        )
    
    # Check if user is already an assistant
    existing_assistant = db.query(model.Assistants).filter(
        model.Assistants.user_id == assistant.user_id
    ).first()
    if existing_assistant:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User {assistant.user_id} is already registered as an assistant"
        )
    
    # Create new assistant
    try:
        new_assistant = model.Assistants(
            name=assistant.name,
            weekly_working_hours=0,  # Initialize with 0 hours
            user_id=assistant.user_id
        )
        
        db.add(new_assistant)
        db.commit()
        db.refresh(new_assistant)
        return new_assistant
        
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/{assistant_id}", response_model=schemas.AssistantResponse, status_code=status.HTTP_200_OK)
async def update_assistant(
    assistant_id: str,
    assistant_update: schemas.AssistantUpdate,
    db: db_dependency,
    current_user: dict = Security(get_current_user)
):
    """Update assistant details (Management role required)"""
    check_management_role(current_user)
    
    # Check if assistant exists
    assistant = db.query(model.Assistants).filter(
        model.Assistants.assistant_id == assistant_id
    ).first()
    if not assistant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Assistant with ID {assistant_id} not found"
        )
    
    try:
        # Update name if provided
        if assistant_update.name is not None:
            assistant.name = assistant_update.name
        
        # Update weekly working hours if provided
        if assistant_update.weekly_working_hours is not None:
            if not (0 <= assistant_update.weekly_working_hours <= 60):  # Assistants can work up to 60 hours
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Weekly working hours must be between 0 and 60"
                )
            assistant.weekly_working_hours = assistant_update.weekly_working_hours
        
        db.commit()
        db.refresh(assistant)
        return assistant
        
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{assistant_id}", status_code=status.HTTP_200_OK)
async def delete_assistant(
    assistant_id: str,
    db: db_dependency,
    current_user: dict = Security(get_current_user)
):
    """Delete an assistant (Management role required)"""
    check_management_role(current_user)
    
    # Check if assistant exists
    assistant = db.query(model.Assistants).filter(
        model.Assistants.assistant_id == assistant_id
    ).first()
    if not assistant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Assistant with ID {assistant_id} not found"
        )
    
    # Check if assistant has any active schedules
    active_schedules = db.query(model.TruckSchedules).filter(
        model.TruckSchedules.assistant_id == assistant_id,
        model.TruckSchedules.status.in_([model.ScheduleStatus.PLANNED, model.ScheduleStatus.IN_PROGRESS])
    ).first()
    
    if active_schedules:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete assistant with active schedules"
        )
    
    try:
        db.delete(assistant)
        db.commit()
        return {"detail": f"Assistant {assistant_id} deleted successfully"}
        
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
