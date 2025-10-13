from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated, List
from uuid import UUID, uuid4
from datetime import datetime, timedelta, date , time 
from app.core.database import get_db
from app.core import model, schemas
import pytz

router = APIRouter(prefix="/truckSchedules")
db_dependency = Annotated[Session, Depends(get_db)]



def get_current_user():
    return {"username": "admin", "role": "Management", "store_id": "store123"}

@router.get("/", response_model=List[schemas.Truck_Schedule], status_code=status.HTTP_200_OK)
def get_all_truck_schedules(db: db_dependency,current_user: dict = Depends(get_current_user)):
    
    role = current_user.get("role")
    if role not in ["StoreManager", "Management", "Admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to view truck schedules"
        )

    truck_schedules = db.query(model.TruckSchedules).all()

    if not truck_schedules:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No truck schedules found"
        )

    return truck_schedules

@router.get("/{schedule_id}", response_model=schemas.Truck_Schedule, status_code=status.HTTP_200_OK)
def get_truck_schedule_by_id( schedule_id: str,db: db_dependency, current_user: dict = Depends(get_current_user)):
    
    role = current_user.get("role")
    if role not in ["StoreManager", "Management", "Admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to view this truck schedule"
        )

    
    truck_schedule = db.query(model.TruckSchedules).filter(model.TruckSchedules.schedule_id == schedule_id).first()
    if not truck_schedule:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Truck schedule with ID {schedule_id} not found"
        )

    return truck_schedule


@router.post("/", response_model=schemas.Truck_Schedule, status_code=status.HTTP_201_CREATED)
def create_truck_schedule(new_truck_schedule: schemas.Truck_Schedule,db: db_dependency,current_user: dict = Depends(get_current_user)):
    # Role check
    if current_user.get("role") != "Management":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Management can create truck schedules"
        )

    
    sl_tz = pytz.timezone("Asia/Colombo")
    min_date = datetime.now(sl_tz).date() + timedelta(days=7)
    scheduled_date = new_truck_schedule.scheduled_date

    if scheduled_date < min_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Departure time must be at least 7 days from today"
        )

    # Ensure duration is an integer (minutes)
    if isinstance(new_truck_schedule.duration, time):
        # Convert time to minutes if a time object was provided
        duration_minutes = new_truck_schedule.duration.hour * 60 + new_truck_schedule.duration.minute
    else:
        duration_minutes = new_truck_schedule.duration

    # Create new truck schedule
    truck_schedule = model.TruckSchedules(
        route_id=new_truck_schedule.route_id,
        truck_id=new_truck_schedule.truck_id,
        driver_id=new_truck_schedule.driver_id,
        assistant_id=new_truck_schedule.assistant_id,
        scheduled_date=new_truck_schedule.scheduled_date,
        departure_time=new_truck_schedule.departure_time,
        duration=duration_minutes,
        status=new_truck_schedule.status
    )

    db.add(truck_schedule)
    db.commit()
    db.refresh(truck_schedule)

    return truck_schedule

@router.put("/{schedule_id}", response_model=schemas.Truck_Schedule, status_code=status.HTTP_200_OK)
def update_truck_schedule(schedule_id: str, update_data: schemas.Truck_Schedule, db: db_dependency, current_user: dict = Depends(get_current_user)):

    if current_user.get("role") != "Management":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Management can update truck schedules"
        )

    # Check if schedule exists
    truck_schedule = db.query(model.TruckSchedules).filter(model.TruckSchedules.schedule_id == schedule_id).first()
    if not truck_schedule:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Truck schedule {schedule_id} not found"
        )
    
    # Validate foreign keys
    if update_data.route_id:
        route = db.query(model.Routes).filter(model.Routes.route_id == update_data.route_id).first()
        if not route:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Route with ID {update_data.route_id} not found"
            )
    
    if update_data.truck_id:
        truck = db.query(model.Trucks).filter(model.Trucks.truck_id == update_data.truck_id).first()
        if not truck:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Truck with ID {update_data.truck_id} not found"
            )
    
    if update_data.driver_id:
        driver = db.query(model.Drivers).filter(model.Drivers.driver_id == update_data.driver_id).first()
        if not driver:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Driver with ID {update_data.driver_id} not found"
            )
    
    if update_data.assistant_id:
        assistant = db.query(model.Assistants).filter(model.Assistants.assistant_id == update_data.assistant_id).first()
        if not assistant:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Assistant with ID {update_data.assistant_id} not found"
            )

    update_dict = update_data.model_dump(exclude_unset=True)

    # Convert status enum if necessary
    if "status" in update_dict:
        update_dict["status"] = update_dict["status"].value if hasattr(update_dict["status"], "value") else update_dict["status"]

    # Validate departure date (at least 7 days from now)
    if "scheduled_date" in update_dict:
        sl_tz = pytz.timezone("Asia/Colombo")
        min_date = datetime.now(sl_tz).date() + timedelta(days=7)
        scheduled_date = update_dict["scheduled_date"]
        if scheduled_date < min_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Scheduled date must be at least 7 days from today"
            )
         

    # Check if there are any existing allocations
    allocations = db.query(model.TruckAllocations).filter(
        model.TruckAllocations.schedule_id == schedule_id
    ).all()
    
    if allocations and truck_schedule.status != update_dict.get('status', truck_schedule.status):
        # Don't allow status changes if there are allocations
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot update schedule status while it has active allocations"
        )

    # Update fields
    for key, value in update_dict.items():
        setattr(truck_schedule, key, value)

    try:
        db.commit()
        db.refresh(truck_schedule)
        return truck_schedule
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )




@router.delete("/{schedule_id}", status_code=status.HTTP_200_OK)
def delete_truck_schedule(schedule_id: str, db: db_dependency, current_user: dict = Depends(get_current_user)):
    # Check role
    if current_user.get("role") != "Management":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Management can delete truck schedules"
        )
    
    # Fetch the schedule
    truck_schedule = db.query(model.TruckSchedules).filter(model.TruckSchedules.schedule_id == schedule_id).first()
    if not truck_schedule:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Truck schedule {schedule_id} not found"
        )
    
    # Delete and commit
    db.delete(truck_schedule)
    db.commit()
    
    return {"detail": f"Truck schedule {schedule_id} deleted successfully"}
