# Create a new APIRouter instance for the 'assets' routes
from typing import List
from fastapi import APIRouter, Depends, Query, Request, status

from src.authorization.authorize import get_user
from src.authorization.models.user import User
import logging

router = APIRouter(prefix="/secure", tags=["Example"])
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Summary of the API",
    description="Detailed description of the API"
)
async def get_all_paginated(
    request: Request,
    page: int = Query(1, description="Page number"),
    page_size: int = Query(20, description="Page size"),
    filters: List[str] = Query([], description="Filters"),
    sort_by: List[str] = Query([], description="Sorting"),
    user: User = Depends(get_user)
):
    return  {
        "message": "Hello, World!",
        "page": page,
        "page_size": page_size,
        "filters": filters,
        "sort_by": sort_by,
        "user": user
    }