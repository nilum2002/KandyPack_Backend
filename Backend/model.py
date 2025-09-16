from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, event, DateTime, Float, Date, Time
from database import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship, sessionmaker
import uuid 


# generate uuid 
def generate_uuid():
    return str(uuid.uuid4())

class Customers(Base):
    __tablename__ = "customers"
    # id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(String(36), primary_key=True, index = True, default=generate_uuid)
    customer_name = Column(String(100))
    phone_number = Column(String(20))
    address = Column(String(200))


class Orders(Base):
    __tablename__ = "orders"
    # id = Column(Integer, primary_key=True, autoincrement=True)
    Order_id = Column(String(36), primary_key=True, index = True, default= generate_uuid)
    customer_id = Column(String(36), ForeignKey("customers.customer_id"))
    order_date = Column(DateTime, default = lambda : datetime.now(timezone.utc))
    deliver_address = Column(String(200))
    status = Column(String(10))
    Deliver_city = Column(String(50))
    full_price = Column(Integer)

class Store(Base):
    __tablename__ = "store"
    store_id = Column(String(36),primary_key=True,index=True, default= generate_uuid )
    telephone_number = Column(String(15))
    name = Column(String(20))
    address = Column(String(255))
    near_railway_station = Column(String(100))
    contact_person = Column(String(100))


class Routes(Base):
    __tablename__ = "routes"
    route_id = Column(String(20), primary_key= True,index=True)
    Order_id = Column(String(36), ForeignKey("orders.Order_id"))
    distance = Column(Integer)
    store_id = Column(String(36), ForeignKey("store.store_id"))
    start_city = Column(String(50))
    end_city = Column(String(50))


class Rout_cities(Base):
    __tablename__ = "route_cities"
    route_city_id = Column(String(50), primary_key=True, index= True)
    city = Column(String(50))
    route_id = Column(String(20),ForeignKey("routes.route_id"))

class Product(Base):
    __tablename__ = "products"
    product_type_id = Column(String(100), primary_key= True, index= True)
    space_consumption_rate = Column(Integer)

class Order_items(Base):
    __tablename__ = "order_items"
    item_id = Column(String(36), primary_key= True, index=True, default= generate_uuid)
    quantity = Column(Integer)
    store_id = Column(String(36), ForeignKey("store.store_id"))
    product_type_id = Column(String(100), ForeignKey("products.product_type_id"))
    item_price = Column(Float)
    Order_id = Column(String(36), ForeignKey("orders.Order_id"))


class City(Base):
    __tablename__ = "city"
    city_id = Column(String(50), primary_key= True, index=True)
    city_name = Column(String(100))
    province = Column(String(100))
    station_id = Column(String(50), ForeignKey("railway_stations.station_name"))


class RailwayStations(Base):
    __tablename__ = "railway_stations"
    station_id = Column(String(50), primary_key= True, index=True)
    station_name = Column(String(100), primary_key= True , index= True )
    city_id = Column(String(50), ForeignKey("city.city_id"))

class Train(Base):
    __tablename__ = "trains"
    train_id = Column(String(50), primary_key= True, index=True)
    train_name = Column(String(100))
    capacity = Column(Integer)

class Train_Schedules(Base):
    __tablename__ = "train_schedules"
    scheduled_id = Column(String(36), primary_key= True, index= True, default= generate_uuid)
    date = Column(DateTime, default = lambda : datetime.now(timezone.utc))
    scheduled_date = Column(Date)
    departure_time = Column(Time)
    arrival_time = Column(Time)
    station_id = Column(String(50), ForeignKey("railway_stations.station_id"))
    train_id = Column(String(50), ForeignKey("trains.train_id"))
    status = Column(String(50))


class RailAllocations(Base):
    __tablename__ = "rail_allocations"
    allocation_id = Column(String(36), primary_key=True, index= True, default=generate_uuid)
    shipment_date = Column(Date)
    status = Column(String(20))
    scheduled_id = Column(String(36), ForeignKey("train_schedules.scheduled_id"))

class Trucks(Base):
    __tablename__ = "trucks"
    truck_id = Column(String(36), primary_key=True, index=True, default= generate_uuid)
    capacity = Column(Integer)
    license_num = Column(String(50))
    is_active = Column(Boolean)

class Assistance(Base):
    __tablename__ = "assistant"
    assistant_id = Column(String(36), primary_key=  True ,index = True, default= generate_uuid)
    name = Column(String(100))
    weekly_working_hours = Column(Integer)
    
class Truck_Schedules(Base):
    __tablename__ = "truck_schedules"
    scheduled_id = Column(String(36), primary_key= True, index= True, default= generate_uuid)
    date = Column(DateTime, default = lambda : datetime.now(timezone.utc))
    scheduled_date = Column(Date)
    departure_time = Column(Time)
    duration = Column(Integer)
    route_id = Column(String(20), ForeignKey("routes.route_id"))
    truck_id = Column(String(36),primary_key= "trucks.truck_id")
    assistant_id = Column(String(36), ForeignKey("assistant.assistant_id"))
    status = Column(String(50))


class Truck_allocations(Base):
    __tablename__ = "truck_allocation"
    allocation_id = Column(String(36), primary_key=True, index=True, default=generate_uuid)
    shipment_date = Column(Date)
    scheduled_id = Column(String(36), ForeignKey("truck_schedules.scheduled_id"))








