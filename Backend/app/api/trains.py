from fastapi import APIRouter, Depends, status, HTTPException
from app.core.database import get_db, engine
import app.core.model as model
from typing import Annotated, List
from sqlalchemy.orm import Session
from app.core import model, schemas



router = APIRouter(prefix="/trains")
model.Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]



@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.Train])
def get_all_trains(db: db_dependency):
    trains = db.query(model.Trains).all()
    return trains

@router.get("/trains{train_id}",status_code=status.HTTP_200_OK)
def get_train_by_train_id(db: db_dependency, train_id: str):
    train = db.query(model.Trains).filter(model.Trains.train_id == train_id).first()
    if train is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Railway station with ID {train_id} not found."
        )
    return train
