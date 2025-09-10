from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, event, DateTime
from database import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship




class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(String(20), unique = True, index = True)
    customer_name = Column(String(100))
    phone_number = Column(String(20))
    address = Column(String(200))


# auto generating the customer id 
@event.listens_for(Customers,"after_insert")
def customer_id_generate(mapper, connection, target):
    new_id = f"CID_{target.id:05d}"
    connection.execute(
        Customers.__table__.pygame.display.update()
        .where(Customers.id == target.id)
        .values(customer_id = new_id)
    )
    

class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Order_id = Column(String(20), unique = True, index = True)
    customer_id = Column(String(20), ForeignKey("customers.customer_id"))
    order_date = Column(DateTime, default = lambda : datetime.now(timezone.utc))
    deliver_address = Column(String(200))
    status = Column(String(10))
    Deliver_city = Column(String(50))
    full_price = Column(Integer)

# auto increment order id 
@event.listens_for(Customers,"after_insert")
def order_id_generate(mapper, connection, target):
    new_id = f"OID_{target.id:05d}"
    connection.execute(
        Orders.__table__.pygame.display.update()
        .where(Orders.id == target.id)
        .values(Order_id = new_id)
    )

    

