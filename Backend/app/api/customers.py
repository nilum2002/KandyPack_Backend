from fastapi import APIRouter, Depends, status, HTTPException
from app.core.database import get_db, engine
import app.core.model as model
from typing import Annotated
from sqlalchemy.orm import Session
from app.core import model, schemas

router = APIRouter(prefix="/customers")
model.Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]

# dummy 
def get_current_user():
    return {"username": "admin", "role": "Management"}  # Replace with real auth

@router.get("/{customer_id}", response_model=schemas.customer, status_code=status.HTTP_200_OK)
def get_customer(customer_id: str, db: db_dependency):
    customer = db.query(model.Customers).filter(model.Customers.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail=f"Customer {customer_id} not found")
    return customer

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_customer(customer: schemas.CustomerCreate, db: db_dependency):
    new_customer = model.Customers(
        customer_name=customer.customer_name,
        phone_number = customer.phone_number,
        address = customer.address
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return {"message": "Customer added successfully", "customer": new_customer}

@router.put("/{customer_id}", response_model=schemas.customer, status_code=status.HTTP_200_OK)
def update_customer(customer_id: str, customer_update: schemas.customerUpdate, db: db_dependency, current_user: dict = Depends(get_current_user)):
    if current_user.get("role") != "Management":
        raise HTTPException(status_code=403, detail="Only Management can update customers")
    
    customer = db.query(model.Customers).filter(model.Customers.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail=f"Customer {customer_id} not found")
    
    update_data = customer_update.model_dump(exclude_unset=True)
    
    update_data["customer_id"] = customer_id
    for key, value in update_data.items():
        setattr(customer, key, value)
    
    db.commit()
    db.refresh(customer)
    return customer

@router.delete("/{customer_id}", status_code=status.HTTP_200_OK)
def delete_customer(customer_id: str, db: db_dependency, current_user: dict = Depends(get_current_user)):
    if current_user.get("role") != "Management":
        raise HTTPException(status_code=403, detail="Only Management can delete customers")
    
    customer = db.query(model.Customers).filter(model.Customers.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail=f"Customer {customer_id} not found")
    
    db.delete(customer)
    db.commit()
    
    return {"detail": f"Customer {customer_id} deleted successfully"}


