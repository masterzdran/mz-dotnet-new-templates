import uuid
from fastapi.openapi.docs import (
    get_redoc_html
)
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from .config.swagger_ui_config import SwaggerUiConfig
from .observability.logging import setup_logging
from .observability.tracing import setup_tracing
from .observability.trace_context import trace_id_var
from .config import get_app_config
from .features.services.health_service.api.v1.service.api_router import health_service_api_router
from .features.services.secure_service.api.v1.service.api_router import secure_service_api_router

app_config = get_app_config()

def create_app() -> FastAPI:
    # Set up logging and tracing
    setup_logging()
    setup_tracing()

    # Set up Entra client ID and scope
    app_client_id = app_config.get_entra_client_id()
    app_client_scope = app_config.get_entra_scope()
    
    app = FastAPI(
        title=SwaggerUiConfig.Title,
        description=SwaggerUiConfig.Description,
        version=SwaggerUiConfig.Version,
        openapi_url=SwaggerUiConfig.OpenApiURL,
        swagger_ui_oauth2_redirect_url="/oauth2-redirect",
        swagger_ui_init_oauth={
            "usePkceWithAuthorizationCodeGrant": True,
            "clientId": f"{app_client_id}",
            "scopes": f"api://{app_client_id}/{app_client_scope}",
        }
    )

    app.mount("/static", StaticFiles(directory="static"), name="static")

    # Set all CORS enabled origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    # Include API routers
    app.include_router(health_service_api_router, prefix=app_config.get_api_v_str())
    app.include_router(secure_service_api_router, prefix=app_config.get_api_v_str())
    return app

app = create_app()

# Middleware to set trace ID
@app.middleware("http")
async def add_trace_id(request: Request, call_next):
    # Generate or get a trace ID (example: using headers or UUID)
    trace_id = request.headers.get("X-Trace-ID", str(uuid.uuid4()))
    
    # Store trace_id in request.state
    request.state.trace_id = trace_id
    trace_id_var.set(trace_id)
    response = await call_next(request)
    return response
@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=SwaggerUiConfig.OpenApiURL,
        title=SwaggerUiConfig.Title,
        redoc_favicon_url="/static/favicon.ico"
    )