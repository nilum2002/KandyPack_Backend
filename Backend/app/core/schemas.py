from pydantic import BaseModel
from typing import Annotated
from app.core.database import engine
import app.core.model as model




model.Base.metadata.create_all(bind= engine)


class userBase(BaseModel):
    user_id: str 
    user_name : str 
    password_hash: str 
    role : str 
    created_at : str 

class customer(BaseModel):
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

class store(BaseModel):
    store_id : str 
    name : str 
    telephone_number : str 
    address : str 
    contact_person : str 
    station_id : str 

class routeBase(BaseModel):
    route_id  : str 
    store_id : str 
    start_city_id : str 
    end_city_id : str 
    distance : int 

class routeOrderBase(BaseModel):
    route_order_id : str 
    route_id : str 
    order_id : str 

class productBase(BaseModel):
    product_type_id : str 
    product_name : str 
    space_consumption_rate : int 

class order_itemsBase(BaseModel):
    item_id : str 
    order_id : str 
    store_id : str 
    product_type_id : str 
    quantity : int 
    item_price: float

class City(BaseModel):
    city_id :str 
    city_name : str
    province : str 
    class Config:
        orm_mode = True

class RailwayStation(BaseModel):
    station_id : str 
    station_name : str 
    city_id : str 
    class Config:
        orm_mode = True

class Train(BaseModel):
    train_id : str 
    train_name : str 
    capacity : int 

class Train_SchedulesBase(BaseModel):
    schedule_id : str 
    train_id : str 
    station_id : str 
    scheduled_date : str 
    departure_time : str 
    arrival_time : str 
    status : str 

class RailwayAllocationBase(BaseModel):
    allocation_id : str 
    order_id : str 
    schedule_id : str 
    shipment_date : str 
    status : str 

class driverBase(BaseModel):
    driver_id : str 
    name : str 
    weekly_working_hours : int 
    user_id : str 

class TruckBase(BaseModel):
    truck_id : str 
    license_num : str 
    capacity : int 
    is_active  : bool

class AssistantBase(BaseModel):
    assistant_id : str 
    name : str 
    weekly_working_hours : str 
    user_id : str 

class Truck_SchedulesBase(BaseModel):
    schedule_id : str 
    route_id : str 
    truck_id : str 
    driver_id : str 
    assistant_id : str 
    scheduled_date : str 
    departure_time : str 
    duration : str 
    status : str 

class Truck_allocationBase(BaseModel):
    allocation_id : str 
    order_id : str 
    schedule_id : str 
    shipment_date : str 
    status  : str 


class CustomerCreate(customer):
    customer_name : str 
    phone_number : str 
    address : str 


class customerUpdate(customer):
    customer_name : str 
    phone_number : str 
    address : str 

class UserCreate(userBase):
    pass


class StoreCreate(BaseModel):
    store_id : str 
    name : str 
    telephone_number : str
    address : str
    contact_person: str 
    station_id : str 

class StoreUpdate(BaseModel):
    name : str 
    telephone_number : str
    address : str
    contact_person: str 
    station_id : str 