from pydantic import BaseModel
from typing import Annotated
from database import engine, Session_local
from sqlalchemy.orm import Session
import model




model.Base.metadata.create_all(bind= engine)


class customerBase(BaseModel):
    customer_id : str 
    customer_name : str 
    phone_number : str 
    address : str 



class orderBase(BaseModel):
    Order_id : str 
    customer_id: str 
    order_date: str 
    deliver_address  : str 
    status : str 
    Deliver_city : str 
    full_price  : int 



def get_db():
    db = Session_local()
    try:
        yield db 
    finally:
        db.close()


