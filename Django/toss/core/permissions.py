from rest_framework import permissions

class IsOwnerOrStaff(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_staff or
            request.user.is_superuser or
            request.user == obj
        )