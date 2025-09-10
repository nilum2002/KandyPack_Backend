import model 
import database
from sqlalchemy.orm import sessionmaker


model.Base.metadata.create_all(database.engine)
def insert_customers():
    Session = sessionmaker(bind= database.engine)
    session = Session()

    new_customer = model.Customers(
    customer_name="Nilum",
    phone_number="0766520743",
    address="Suraweeragewatta,Dandeniya,Urugamuwa"
    )
    session.add(new_customer)
    session.commit()
    print("Inserted successfully!")

def insert_orders():
    Session = sessionmaker(bind= database.engine)
    session = Session()

    new_order = model.Orders(
    customer_id="CID_00001",
    deliver_address="Suraweeragewatta,Dandeniya,Urugamuwa",
    status = "pending", 
    Deliver_city = "Kandy", 
    full_price = 100
    )
    session.add(new_order)
    session.commit()
    print("Inserted order successfully!")

insert_orders()