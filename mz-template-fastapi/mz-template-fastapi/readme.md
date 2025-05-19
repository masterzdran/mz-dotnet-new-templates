# FastAPI Project Template

A production-ready FastAPI project template featuring:

- Modular service structure
- Azure AD JWT authentication and role-based authorization
- OpenTelemetry logging and tracing
- Environment-based configuration
- Docker support
- Pre-commit hooks and type checking
- Example health and secure endpoints

---

## Project Structure

```
src/
  main.py                # FastAPI app entrypoint
  config/                # App configuration and settings
  authorization/         # Azure AD auth, user/role models
  features/              # Modular service features (health, secure, etc.)
  observability/         # Logging and tracing setup
static/                  # Static assets (e.g., logo, favicon)
tests/                   # Unit tests
Dockerfile
docker-compose.yml
requirements.txt
.env / sample.env
.pre-commit-config.yaml
```

---

## Setup Instructions

### Prerequisites

- Python 3.11.9
- Docker (optional, for containerized deployment)

### Installation

1. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Copy `sample.env` to `.env` and fill in required environment variables.

---

### Running the Application

- Start the FastAPI app:
    ```sh
    uvicorn src.main:app --reload
    ```
- Access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger UI: `/docs`
- ReDoc: `/redoc`

---

### Running with Docker

1. Build the Docker image:
    ```sh
    docker build -t fastapi-project .
    ```
2. Run the container:
    ```sh
    docker run -p 8000:80 fastapi-project
    ```

---

### Running Tests

```sh
python -m unittest discover -s tests
```

---

### Debugging

- Use the provided VSCode launch configuration (`.vscode/launch.json`).

---

### Pre-commit Hooks

1. Install hooks:
    ```sh
    pre-commit install
    ```
2. Run hooks manually:
    ```sh
    pre-commit run --all-files
    ```

---

## Configuration

- All configuration is managed in [src/config/settings.py](src/config/settings.py) and [src/config/appconfig.py](src/config/appconfig.py).
- Environment variables are loaded from `.env` (see [sample.env](sample.env)).

---

## Authentication & Authorization

- Azure AD JWT validation is implemented in [src/authorization/azure_authorization.py](src/authorization/azure_authorization.py).
- Role-based access is managed via [src/authorization/authoriza.py](src/authorization/authoriza.py) and [src/authorization/models/app_roles.py](src/authorization/models/app_roles.py).

---

## Logging and Tracing

- Logging: [src/observability/logging.py](src/observability/logging.py)
- Tracing: [src/observability/tracing.py](src/observability/tracing.py)

---

## Example Endpoints

- Health check: `/api/v1/healthcheck`
- Secure endpoint (requires Azure AD auth): `/api/v1/secure`

---

## License

This project is licensed under the MIT License.
