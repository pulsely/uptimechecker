from rest_framework.permissions import BasePermission


def operator_privilege_check(user):
    # return (user.is_authenticated and (user.role in ['staff', 'admin'] or user.is_staff))
    return user.is_authenticated and (user.role in ['user', 'admin'] or user.is_staff)

def staff_privilege_check(user):
    # return (user.is_authenticated and (user.role in ['staff', 'admin'] or user.is_staff))
    return user.is_authenticated and (user.role in [ 'admin'] or user.is_staff)

class IsOperatorAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class IsStaffAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (
                    request.user.role in ['admin', ] or request.user.is_staff))
