from enum import Enum

class AppRoles(str, Enum):
    ROLE_USER = "ROLE_USER"
    ROLE_CONTRIBUTOR = "ROLE_CONTRIBUTOR"
    ROLE_MEMBER = "ROLE_MEMBER"
    ROLE_ADMIN = "ROLE_ADMIN"
