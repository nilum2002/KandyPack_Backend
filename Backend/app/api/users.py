from fastapi import APIRouter, Depends, status, HTTPException
from app.core.database import get_db, engine
import app.core.model as model
from typing import Annotated
from sqlalchemy.orm import Session
from app.core import model, schemas

router = APIRouter(prefix="/users")
model.Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserCreate, db: db_dependency):
    existing_user = db.query(model.Users).filter(model.Users.user_name == user.user_name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = model.Users(
        user_name = user.user_name,
        password_hash=user.password_hash,
        role = user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "new user added successfully", "customer": new_user}

