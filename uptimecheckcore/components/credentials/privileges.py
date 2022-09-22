

from rest_framework.permissions import BasePermission

def operator_privilege_check(user):
    # return (user.is_authenticated and (user.role in ['staff', 'admin'] or user.is_staff))
    return user.is_authenticated and (user.role in ['user', 'admin'] or user.is_staff)


class IsOperatorAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
