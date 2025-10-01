from fastapi import APIRouter


router = APIRouter(prefix="/customers")


@router.get("/")
async def get_customers():
    return {"Massage": "success"}