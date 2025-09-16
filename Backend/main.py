from pydantic import BaseModel
from typing import Annotated
from database import engine, Session_local
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

class storeBase(BaseModel):
    store_id : str
    telephone_number : str 
    name : str 
    address : str 
    near_railway_station : str 
    contact_person : str 

class routeBase(BaseModel):
    route_id : str
    Order_id : str 
    distance : str 
    store_id : str 
    start_city : str 
    end_city : str 

class route_cityBase(BaseModel):
    route_city_id : str 
    city : str 
    route_id : str

class productBase(BaseModel):
    product_type_id : str 
    space_consumption_rate : int

class order_itemsBase(BaseModel):
    item_id : str
    quantity : int
    store_id : str 
    product_type_id : str 
    item_price : float
    Order_id : str 

class CityBase(BaseModel):
    city_id :str 
    city_name : str
    province : str 
    station_id : str  

class RailwaystationBase(BaseModel):
    station_id : str
    station_name : str 
    city_id : str 

class TrainBase(BaseModel):
    train_id : str 
    train_name : str 
    capacity : int 

class Train_SchedulesBase(BaseModel):
    scheduled_id : str 
    date : str 
    scheduled_date : str 
    departure_time : str 
    arrival_time : str 
    station_id : str 
    train_id : str 
    status : str 

class RailwayAllocationBase(BaseModel):
    allocation_id : str 
    shipment_date : str 
    status : str 
    scheduled_id : str 

class TruckBase(BaseModel):
    truck_id : str 
    capacity : int
    license_num : str 
    is_active : bool

class AssistantBase(BaseModel):
    assistant_id : str 
    name : str 
    weekly_working_hours : int 

class Truck_SchedulesBase(BaseModel):
    scheduled_id : str 
    date : str 
    scheduled_date : str 
    departure_time : str 
    duration : int 
    route_id : str 
    truck_id : str 
    assistant_id : str
    status : str 

class Truck_allocationBase(BaseModel):
    allocation_id : str 
    shipment_date : str 
    scheduled_id : str 

def get_db():
    db = Session_local()
    try:
        yield db 
    finally:
        db.close()


