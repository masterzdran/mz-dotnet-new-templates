from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def setup_middleware(app: FastAPI) -> None:
    """
    Set up all middleware for the application
    
    Args:
        app: The FastAPI application
    """
    # Get allowed origins from environment
    frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
    allowed_origins = [frontend_origin]
    
    # Setup CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )