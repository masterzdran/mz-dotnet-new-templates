from fastapi import APIRouter
from . import health_service


health_service_api_router = APIRouter()
health_service_api_router.include_router(health_service.router)