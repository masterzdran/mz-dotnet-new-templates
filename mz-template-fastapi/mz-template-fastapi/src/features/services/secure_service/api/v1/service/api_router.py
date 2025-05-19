from fastapi import APIRouter
from . import secure_service
secure_service_api_router = APIRouter()
secure_service_api_router.include_router(secure_service.router)