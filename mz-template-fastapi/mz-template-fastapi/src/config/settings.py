import os
import logging
from dotenv import load_dotenv

class Settings:
    REQUIRED_VARS = [
        "DATABASE_URL",
        "STORAGE_ACCOUNT_URL",
        "ENTRA_TENANT_ID",
        "ENTRA_CLIENT_ID",
        "ENTRA_SCOPE",
        "AAD_INSTANCE"
        ]

    def __init__(self):
        self.config = {}
        self.load_env_variables()

    def load_env_variables(self):
        load_dotenv()  # Load environment variables from .env file

        for var in self.REQUIRED_VARS:
            value = os.getenv(var)
            if value is None:
                logging.error(f"Environment variable '{var}' was not loaded.")
            else:
                self.config[var] = value