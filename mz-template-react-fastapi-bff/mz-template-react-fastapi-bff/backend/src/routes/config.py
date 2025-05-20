from fastapi import APIRouter, Depends, HTTPException, status
from ..utils.security import verify_api_key
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

router = APIRouter()

@router.get("/config", dependencies=[Depends(verify_api_key)])
async def get_config():
    """
    Get protected configuration data
    
    This endpoint returns sensitive configuration data that should
    only be accessible by authenticated clients with a valid API key.
    """
    try:
        # Get configuration from environment variables
        entra_client_id = os.getenv("ENTRA_CLIENT_ID")
        entra_scope = os.getenv("ENTRA_SCOPE")
        
        if not entra_client_id or not entra_scope:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Server configuration error: Missing required environment variables"
            )
        
        # Return configuration data
        return {
            "entra_client_id": entra_client_id,
            "entra_scope": entra_scope,
            "timestamp": "2025-05-20T12:00:00Z",  # Example timestamp
            "is_enabled": True
        }
    
    except Exception as e:
        # Log the error (in a real app, use proper logging)
        print(f"Error retrieving config: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )