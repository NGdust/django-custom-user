from rest_framework.permissions import BasePermission

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or (request.user and request.user.is_authenticated):
            return True
        return False


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or (request.user and request.user.is_authenticated and request.user.is_superuser):
            return True
        return False
