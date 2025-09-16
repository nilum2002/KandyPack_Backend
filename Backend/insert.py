import model 
import database
from sqlalchemy.orm import sessionmaker


model.Base.metadata.create_all(database.engine)
def insert_customers():
    Session = sessionmaker(bind=database.engine)
    session = Session()

    customers = [
        model.Customers(
            customer_name="Kavindu Perera",
            phone_number="0771234567",
            address="123 Galle Road, Colombo"
        ),
        model.Customers(
            customer_name="Dilani Fernando",
            phone_number="0712345678",
            address="45 Temple Lane, Kandy"
        ),
        model.Customers(
            customer_name="Sahan Jayasinghe",
            phone_number="0759876543",
            address="67 Beach Road, Negombo"
        ),
        model.Customers(
            customer_name="Tharushi Senanayake",
            phone_number="0763456789",
            address="89 Lake View, Kurunegala"
        ),
        model.Customers(
            customer_name="Nipun Silva",
            phone_number="0784567890",
            address="21 Station Road, Galle"
        ),
        model.Customers(
            customer_name="Ishara de Silva",
            phone_number="0728765432",
            address="9 Central Street, Matara"
        ),
        model.Customers(
            customer_name="Chathura Ranasinghe",
            phone_number="0701239876",
            address="34 Market Road, Anuradhapura"
        ),
        model.Customers(
            customer_name="Harini Wickramasinghe",
            phone_number="0745671234",
            address="56 Hospital Lane, Ratnapura"
        ),
        model.Customers(
            customer_name="Ravindu Gunasekara",
            phone_number="0719988776",
            address="77 Temple Road, Jaffna"
        ),
        model.Customers(
            customer_name="Sasini Karunaratne",
            phone_number="0753344556",
            address="12 Hill Street, Nuwara Eliya"
        )
    ]

    session.add_all(customers)
    session.commit()
    print("10 Customers inserted successfully!")

# def insert_routes():
#     Session = sessionmaker(bind = database.engine)
#     session = Session()

#     routes = [
#         model.Routes(
#             route_id = "RID_001"
#             Order_id = "0d50ee1c-c5ba-49a7-89e9-ff66885f9210"
#             distance = 10
#             store_id = "ST_0001"
#             start_city = "Kandy"
#             end_city = "Colombo"
#         )
#         model.Routes(
#             route_id = "RID_002"
#             Order_id = "0d50ee1c-c5ba-49a7-89e9-ff66885f9210"
#             distance = 10
#             store_id = "ST_0001"
#             start_city = "Kandy"
#             end_city = "Colombo"
#         )
#         model.Routes(
#             route_id = "RID_001"
#             Order_id = "0d50ee1c-c5ba-49a7-89e9-ff66885f9210"
#             distance = 10
#             store_id = "ST_0001"
#             start_city = "Kandy"
#             end_city = "Colombo"
#         )
#         model.Routes(
#             route_id = "RID_001"
#             Order_id = "0d50ee1c-c5ba-49a7-89e9-ff66885f9210"
#             distance = 10
#             store_id = "ST_0001"
#             start_city = "Kandy"
#             end_city = "Colombo"
#         )
#         model.Routes(
#             route_id = "RID_001"
#             Order_id = "0d50ee1c-c5ba-49a7-89e9-ff66885f9210"
#             distance = 10
#             store_id = "ST_0001"
#             start_city = "Kandy"
#             end_city = "Colombo"
#         )

#     ]
#     session.add_all(routes)
#     session.commit()
#     print("Inserted successfully")


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

def insert_orders():
    Session = sessionmaker(bind=database.engine)
    session = Session()

    # List of customer IDs
    customer_ids = [
        "096165ab-8f34-41e4-8aac-7eece9e73ebb",
        "2003299e-6edd-47fe-b25d-0c70e7ac5a1e",
        "3af8ae3d-1706-4d31-abed-b2793805f7ea",
        "45a0d904-ad11-4f1c-a18f-9d235be1ccc5",
        "53bc32cd-06ca-4ada-b6a3-f28fafe55840",
        "9ee1d9b0-b3f1-4136-9c4a-d1b40fb28091",
        "ae2c89b0-34f2-4ce0-b087-93bd6286a9b9",
        "aeeff2e3-d47a-41ed-aba7-f63423e8e7ce",
        "b89ee389-998c-4d15-9951-66ba643dde95",
        "c00d9e7f-1281-44d4-b0eb-7dde45563b49"

    ]

    # Example data for each order
    orders = [
        model.Orders(
            customer_id=customer_ids[0],
            deliver_address="123 Galle Road, Colombo",
            status="pending",
            Deliver_city="Colombo",
            full_price=2500
        ),
        model.Orders(
            customer_id=customer_ids[1],
            deliver_address="45 Temple Lane, Kandy",
            status="delivered",
            Deliver_city="Kandy",
            full_price=1800
        ),
        model.Orders(
            customer_id=customer_ids[2],
            deliver_address="67 Beach Road, Negombo",
            status="pending",
            Deliver_city="Negombo",
            full_price=2200
        ),
        model.Orders(
            customer_id=customer_ids[3],
            deliver_address="89 Lake View, Kurunegala",
            status="delivered",
            Deliver_city="Kurunegala",
            full_price=1500
        ),
        model.Orders(
            customer_id=customer_ids[4],
            deliver_address="21 Station Road, Galle",
            status="pending",
            Deliver_city="Galle",
            full_price=3000
        ),
        model.Orders(
            customer_id=customer_ids[5],
            deliver_address="9 Central Street, Matara",
            status="pending",
            Deliver_city="Matara",
            full_price=2000
        ),
        model.Orders(
            customer_id=customer_ids[6],
            deliver_address="34 Market Road, Anuradhapura",
            status="delivered",
            Deliver_city="Anuradhapura",
            full_price=2700
        ),
        model.Orders(
            customer_id=customer_ids[7],
            deliver_address="56 Hospital Lane, Ratnapura",
            status="pending",
            Deliver_city="Ratnapura",
            full_price=1900
        ),
        model.Orders(
            customer_id=customer_ids[8],
            deliver_address="12 Temple Road, Jaffna",
            status="pending",
            Deliver_city="Jaffna",
            full_price=2300
        ),
        model.Orders(
            customer_id=customer_ids[9],
            deliver_address="78 Hill Street, Nuwara Eliya",
            status="delivered",
            Deliver_city="Nuwara Eliya",
            full_price=2500
        )
    ]

    session.add_all(orders)
    session.commit()
    print("10 Orders inserted successfully!")


# insert_customers()
insert_orders()