from fastapi import APIRouter, status
from src.observability.trace_context import trace_id_var
import logging


router = APIRouter(prefix="/healthcheck", tags=["Monitoring"])
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Get health check",
    description="Validate if the service is available",
    response_description="healthy if service is available, unhealthy otherwise"
)
async def healthcheck():
    # validation logic
    return {"status": "healthy"} 