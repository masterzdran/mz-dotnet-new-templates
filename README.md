# mz-dotnet-new-templates

A collection of project accelerators for quickly bootstrapping new projects using the `dotnet new` templating system.

## Available Templates

- **Python: FastAPI Project Template**  
  A production-ready FastAPI template with modular structure, Azure AD authentication, OpenTelemetry, Docker support, and more.

- **React + FastAPI BFF Project Template**  
  A secure, full-stack template with a React frontend and FastAPI backend, featuring runtime config injection, API key protection, CORS, Docker support, and VSCode debugging.

---

## Installation

### Install from Local Repository

To install these templates globally using the .NET CLI:

```sh
dotnet new install <PATH_TO_THIS_REPOSITORY>
```
Replace `<PATH_TO_THIS_REPOSITORY>` with the local path or git URL of this repository.

### Install from NuGet (Recommended)

You can also install the template package directly from NuGet:

```sh
dotnet new install masterzdran.fastapi.project.accelerator::1.0.0
dotnet new install masterzdran.react.fastapi.project.accelerator::1.0.0
```

---

## Usage

After installation, create a new project using your chosen template:

- **FastAPI only:**
  ```sh
  dotnet new masterzdran.fastapi.project.accelerator -n MyFastApiApp
  ```

- **React + FastAPI BFF:**
  ```sh
  dotnet new masterzdran.react.fastapi.project.accelerator -n MyReactFastApiBffApp
  ```

---

## Template Features

### FastAPI Template
- Modular FastAPI structure
- Azure AD JWT authentication and role-based authorization
- OpenTelemetry logging and tracing
- Docker and Docker Compose support
- Pre-commit hooks and type checking
- Example health and secure endpoints

### React + FastAPI BFF Template
- Secure runtime config injection (no secrets in frontend builds)
- API key protection and CORS enforcement
- React 18 + Vite + TypeScript frontend
- FastAPI backend with environment-based config
- Dockerized full-stack setup
- VSCode launch configs for full-stack debugging

---

## Contributors
* [@masterzdran](https://github.com/masterzdran)

---

## Attribution 
* <a href="https://www.flaticon.com/free-icons/api" title="api icons">Api icons created by Rahat - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/template" title="template icons">Template icons created by Eucalyp - Flaticon</a>
* <a href="https://www.flaticon.com/free-icons/page-design" title="page design icons">Page design icons created by iconsmind - Flaticon</a>