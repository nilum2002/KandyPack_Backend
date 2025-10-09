# app/api/__init__.py
from fastapi import APIRouter


from app.api.customers import router as customer_router
from app.api.users import router as user_router
from app.api.cities import router as city_router
from app.api.railway_stations import router as railway_stations
from app.api.stores import router as stores
from app.api.trains import router as trains



api_router = APIRouter()
api_router.include_router(customer_router)
api_router.include_router(user_router)
api_router.include_router(city_router)
api_router.include_router(railway_stations)
api_router.include_router(stores)
api_router.include_router(trains)

