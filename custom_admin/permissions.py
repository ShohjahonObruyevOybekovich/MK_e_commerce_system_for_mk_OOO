from rest_framework.permissions import BasePermission
from account.models import UserRole


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        try:
            user_role = UserRole.objects.get(user=request.user).role.name
        except UserRole.DoesNotExist:
            return False

        return user_role.lower() == "admin"
