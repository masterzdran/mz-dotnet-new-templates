# Build stage
FROM python:3.11-slim-buster as builder

# Set build arguments and environment variables
ARG APP_USER=appuser
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    postgresql-client \
    libpq-dev \  
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

WORKDIR /

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim-buster

ARG APP_USER=appuser

# Create non-root user
RUN useradd -m -s /bin/bash ${APP_USER}

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    libpq5 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy dependencies
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

# Copy application code and assets with proper structure
COPY --chown=${APP_USER}:${APP_USER} ./src /src
COPY --chown=${APP_USER}:${APP_USER} ./static /static

# Set proper permissions
RUN chown -R ${APP_USER}:${APP_USER} /src /static

USER ${APP_USER}

WORKDIR /

# Create volume mount points
VOLUME ["/data", "/static"]

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:80/api/v1/healthcheck/ || exit 1

EXPOSE 80
# Update the value
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]
