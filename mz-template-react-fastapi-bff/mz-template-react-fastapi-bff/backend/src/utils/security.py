from fastapi import HTTPException, Header, status
import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()

def get_api_key() -> str:
    """
    Get the API key from environment variables
    
    Returns:
        str: The API key
    
    Raises:
        RuntimeError: If the API key is not set
    """
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise RuntimeError("API_KEY environment variable is not set")
    return api_key

async def verify_api_key(x_api_key: Optional[str] = Header(None)) -> None:
    """
    Verify that the API key is valid
    
    Args:
        x_api_key: The API key from the request header
    
    Raises:
        HTTPException: If the API key is invalid or missing
    """
    expected_api_key = get_api_key()
    
    # Check if API key is provided
    if not x_api_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="API key is missing"
        )
    
    # Validate API key
    if x_api_key != expected_api_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key"
        )
    
    # If we reach here, the API key is valid
    return None