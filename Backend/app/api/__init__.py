# app/api/__init__.py
from fastapi import APIRouter


from app.api.customers import router as customer_router
from app.api.users import router as user_router

api_router = APIRouter()
api_router.include_router(customer_router)
api_router.include_router(user_router)
