from rest_framework.permissions import BasePermission


class IsAuthenticatedAdmin(BasePermission):
    """
    Allows access only to authenticated admins.
    """
    message = 'Only for authenticated admins!'

    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 1)
