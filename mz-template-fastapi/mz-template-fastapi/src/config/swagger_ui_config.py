from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI
from typing import Dict, Any

class SwaggerUiConfig:
    Title="API Titles"
    Description="API Description."
    Version="1.0.0"
    OpenApiURL="/openapi.json"
    OpenApiDocsURL="/docs"
    OpenApiReadDocsURL="/redoc"
    LogoOpenApiSchemaURL="/static/logo.png"
    Summary="API summary."

