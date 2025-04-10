from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.filter(name='Moderator').exists():
            return True
        else:
            raise PermissionDenied(detail={
                "error": {
                    "ru": "У вас нет прав доступа к этой операции.",
                    "en": "You do not have permission to perform this operation."
                }
            }, code=403)
