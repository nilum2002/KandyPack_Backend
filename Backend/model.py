from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, event, DateTime
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
    customer_id = Column(String(36), primary_key=True, index = True, default=generate_uuid())
    customer_name = Column(String(100))
    phone_number = Column(String(20))
    address = Column(String(200))

class Orders(Base):
    __tablename__ = "orders"
    # id = Column(Integer, primary_key=True, autoincrement=True)
    Order_id = Column(String(36), primary_key=True, index = True, default= generate_uuid)
    customer_id = Column(String(20), ForeignKey("customers.customer_id"))
    order_date = Column(DateTime, default = lambda : datetime.now(timezone.utc))
    deliver_address = Column(String(200))
    status = Column(String(10))
    Deliver_city = Column(String(50))
    full_price = Column(Integer)


    




