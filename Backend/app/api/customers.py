from fastapi import APIRouter, Depends, status
from app.core.database import get_db, engine
import app.core.model as model
from typing import Annotated
from sqlalchemy.orm import Session
from app.core import model, schemas

router = APIRouter(prefix="/customers")
model.Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]



@router.get("/")
async def get_customers():
    return {"Massage": "success"}


# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_customer(customer: schemas.CustomerCreate, db: db_dependency):
#     new_customer = model.Customers(
#         name=customer.customer_name,
#         email=customer.phone_number,
#         address=customer.address
#     )
#     db.add(new_customer)
#     db.commit()
#     db.refresh(new_customer)
#     return {"message": "Customer added successfully", "customer": new_customer}
