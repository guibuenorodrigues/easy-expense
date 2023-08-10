from fastapi import APIRouter
from app.src.endpoints.v1 import users as users_v1

router = APIRouter()
router.include_router(users_v1.router)
