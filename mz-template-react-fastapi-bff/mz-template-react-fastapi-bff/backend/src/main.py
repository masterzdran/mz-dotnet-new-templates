from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .middleware import setup_middleware
from .routes.config import router as config_router

app = FastAPI(title="Secure Config API")

# Setup middleware (CORS, etc.)
setup_middleware(app)

# Include API routes
app.include_router(config_router, prefix="/api")

# Setup public config.json endpoint that delivers the API key
@app.get("/config.json")
async def get_public_config():
    """
    Public endpoint that returns the API key.
    This simulates runtime injection of the API key into the frontend.
    """
    from .utils.security import get_api_key
    
    return JSONResponse(content={
        "apiKey": get_api_key()
    })

@app.get("/")
async def root():
    """Root endpoint for health check"""
    return {"status": "API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)