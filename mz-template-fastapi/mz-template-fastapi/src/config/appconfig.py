from .settings import Settings
# Singleton pattern to ensure only one instance of AppConfig is created
_app_config_instance = None

def get_app_config():
    global _app_config_instance
    if _app_config_instance is None:
        _app_config_instance = AppConfig()
    return _app_config_instance

class AppConfig:
    def __init__(self):
        self.settings = Settings()  # Instantiate Settings inside AppConfig

    def get_database_url(self):
        return self.settings.config.get("DATABASE_URL", "DATABASE_URL Not Set")

    def get_storage_url(self):
        return self.settings.config.get("STORAGE_ACCOUNT_URL", "STORAGE_ACCOUNT_URL Not Set")
    
    def get_storage_account_container_name(self):
        return self.settings.config.get("STORAGE_ACCOUNT_CONTAINER_NAME", "DEFAULT_DOCUMENT_LOCATION")
    
    def get_api_v_str(self):
        return self.settings.config.get("API_V1_STR", "/api/v1")
    
    def get_project_name(self):
        return self.settings.config.get("PROJECT_NAME", "FastAPI Project Template")
    
    def get_entra_tenant_id(self):
        return self.settings.config.get("ENTRA_TENANT_ID", "ENTRA_TENANT_ID Not Set")
    
    def get_entra_client_id(self):
        return self.settings.config.get("ENTRA_CLIENT_ID", "ENTRA_CLIENT_ID Not Set")

    def get_entra_scope(self):
        return self.settings.config.get("ENTRA_SCOPE", "ENTRA_SCOPE Not Set")

    def get_aad_instance(self):
        return self.settings.config.get("AAD_INSTANCE", "https://login.microsoftonline.com")

    def get__api_audience(self):
        app_client_id = self.get_entra_client_id()
        return self.settings.config.get("API_AUDIENCE", f"api://{app_client_id}")
    
    def get_scope_name(self):
        app_client_id = self.get_entra_client_id()
        app_client_scope = self.get_entra_scope()
        return self.settings.config.get("SCOPE_NAME",  f"api://{app_client_id}/{app_client_scope}")
    
    def get_app_user_role(self):
        return self.settings.config.get("ROLE_USER",  "DEFAULT_APP_USER")

    def get_app_contributor_role(self):
        return self.settings.config.get("ROLE_CONTRIBUTER",  "DEFAULT_APP_CONTRIBUTER")
    
    def get_app_member_role(self):
        return self.settings.config.get("ROLE_MEMBER",  "DEFAULT_APP_MEMBER")
    
    def get_app_admin_role(self):
        return self.settings.config.get("ROLE_ADMIN",  "DEFAULT_APP_ADMIN")

