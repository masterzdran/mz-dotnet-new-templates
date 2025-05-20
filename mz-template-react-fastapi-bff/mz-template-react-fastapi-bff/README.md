# Secure Config Management Example Project

This project demonstrates a secure architecture for handling configuration and secrets in a full-stack application. It consists of a FastAPI backend and a React/TypeScript frontend, both designed to follow security best practices for managing sensitive configuration.

## Architecture Overview

![Architecture Diagram]

### Key Security Features

1. **Runtime Config Injection**: Sensitive information is only delivered at runtime, not baked into builds
2. **API Key Protection**: Backend endpoints are protected by an API key
3. **CORS Protection**: Backend only accepts requests from authorized origins
4. **Environment Variable Management**: All secrets are stored in environment variables, not in code
5. **Secure Frontend Fetch Pattern**: Frontend securely retrieves and uses API keys

## Project Structure

```
.
├── backend/                  # FastAPI Python backend
│   ├── app/                  # Application code
│   │   ├── __init__.py
│   │   ├── main.py           # Main FastAPI application
│   │   ├── middleware.py     # CORS and other middleware
│   │   ├── routes/           # API routes
│   │   │   ├── __init__.py
│   │   │   └── config.py     # Config endpoints
│   │   └── utils/            # Utility functions
│   │       ├── __init__.py
│   │       └── security.py   # API key validation
│   ├── .env.example          # Example environment variables
│   └── requirements.txt      # Python dependencies
│
├── frontend/                 # React/TypeScript frontend
│   ├── index.html            # Entry HTML file
│   ├── package.json          # npm dependencies and scripts
│   ├── tsconfig.json         # TypeScript configuration
│   ├── vite.config.ts        # Vite configuration
│   └── src/                  # Source code
│       ├── App.tsx           # Main application component
│       ├── main.tsx          # Entry point
│       ├── api/              # API client code
│       │   └── index.ts      # API client implementation
│       └── components/       # React components
│           └── ConfigDisplay.tsx  # Display fetched config
│
├── .vscode/                  # VSCode configuration
│   └── launch.json           # Debug configurations
│
└── README.md                 # This file
```

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Python 3.10+
- Visual Studio Code (recommended for debugging)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Linux/Mac
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```

5. Modify the `.env` file with your actual values:
   ```
   API_KEY=your_secure_api_key_here
   ENTRA_CLIENT_ID=your_entra_client_id
   ENTRA_SCOPE=api://your-app-id/access_as_user
   FRONTEND_ORIGIN=http://localhost:5173
   ```

6. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

The backend will be available at `http://localhost:8000`.

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:5173`.

## How Runtime Config Injection Works

This project implements a secure pattern for handling configuration:

1. The backend reads sensitive information from environment variables at startup
2. The frontend makes an initial request to `/config.json` to obtain the API key
3. The frontend stores this API key in memory (not localStorage or cookies)
4. Subsequent API calls include the API key in the `x-api-key` header
5. Protected endpoints verify this API key before returning sensitive configuration

This approach ensures:
- No secrets are embedded in frontend builds
- API keys are delivered at runtime, not build time
- Configuration can be updated without rebuilding the frontend
- The API is protected from unauthorized access

## Security Considerations

### Why Secrets Should Never Be Stored in Frontend Build

Frontend code is always accessible to users through browser dev tools. Any secret baked into a frontend build (whether in JS bundles, environment variables loaded at build time, or hardcoded values) can be extracted by users. This project demonstrates the correct pattern: retrieving sensitive information at runtime from a protected API.

### API Key Injection at Runtime

Instead of hardcoding the API key in the frontend, this application:
1. Exposes a public endpoint (`/config.json`) that provides the API key
2. Injects this key into the HTML response dynamically from server environment variables
3. The frontend fetches this configuration on startup and uses it for subsequent API calls

This approach allows the API key to be rotated without rebuilding the frontend.

### CORS Protection

Cross-Origin Resource Sharing (CORS) protection is implemented to prevent browsers from making requests to the API from unauthorized origins. The backend only accepts requests from the specified frontend origin (e.g., `http://localhost:5173` for development), blocking requests from malicious sites.

## Debugging with VSCode

This project includes VSCode launch configurations for debugging both the backend and frontend simultaneously:

1. Open the project in VSCode
2. Navigate to the Debug panel (Ctrl+Shift+D or Cmd+Shift+D)
3. Select "Debug Full Stack" from the dropdown
4. Press F5 to start debugging

You can set breakpoints in both Python and TypeScript code, and VSCode will stop at both.

To debug individually:
- Select "Debug Backend" to debug only the FastAPI backend
- Select "Debug Frontend" to debug only the React frontend

## Troubleshooting

### 404 Not Found for `/config.json`

If you encounter a 404 error when the frontend tries to fetch `/config.json`:

1. **Check if the backend is running**: Ensure the FastAPI server is running on port 8000.
2. **Verify CORS settings**: Make sure the `FRONTEND_ORIGIN` in your backend `.env` file matches your frontend URL (default: `http://localhost:5173`).
3. **Check Vite proxy settings**: The `/config.json` endpoint should be proxied to the backend in development.
4. **Try direct access**: Open `http://localhost:8000/config.json` in your browser to see if the backend serves it correctly.
5. **Environment variables**: Ensure the API_KEY is properly set in your backend `.env` file.

### API Key Issues

If you successfully get `/config.json` but subsequent API calls fail:

1. **Check browser console**: Look for error messages related to the API key.
2. **Verify headers**: Make sure the `x-api-key` header is being correctly added to requests.
3. **Backend logs**: Check the backend terminal for any authorization errors.

### Backend Connection Issues

If the frontend can't connect to the backend:

1. **Port conflicts**: Make sure no other services are using port 8000.
2. **Proxy settings**: Verify that Vite is correctly proxying requests to the backend.
3. **NetworkError**: If you see network errors, ensure the backend is running and accessible.

### General Debugging Steps

1. **Clear browser cache**: Try hard-refreshing the page (Ctrl+F5).
2. **Check browser console**: Look for error messages or failed network requests.
3. **Inspect network traffic**: Use the Network tab in browser dev tools to see the actual requests and responses.
4. **Restart services**: Sometimes restarting both frontend and backend resolves issues.
5. **Check package versions**: Ensure your Node.js and Python versions are compatible with the project requirements.