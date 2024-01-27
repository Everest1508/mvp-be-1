# permissions.py
from rest_framework.permissions import BasePermission

class IsJWTAuthenticatedPermission(BasePermission):
    def has_permission(self, request, view):
        return request.auth is not None
