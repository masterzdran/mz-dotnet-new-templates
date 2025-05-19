from typing import Any

from fastapi import Depends, HTTPException, status

from .models.user import User
from .models.app_roles import AppRoles
from .azure_authorization import authorize


class ForbiddenAccess(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail=detail, 
            headers={"WWW-Authenticate": "Bearer"})


def get_user(user: User = Depends(authorize)) -> User:
    return user

def get_contributor_user(user: User = Depends(authorize)) -> User:
    if AppRoles.ROLE_CONTRIBUTOR.value in user.roles:
        return user
    raise ForbiddenAccess('Contributor privileges required')

def get_member_user(user: User = Depends(authorize)) -> User:
    if AppRoles.ROLE_MEMBER.value in user.roles:
        return user
    raise ForbiddenAccess('Member privileges required')


def get_admin_user(user: User = Depends(authorize)) -> User:
    if AppRoles.ROLE_ADMIN.value in user.roles:
        return user
    raise ForbiddenAccess('Admin privileges required')