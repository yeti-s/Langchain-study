from rest_framework import permissions

class IsOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.id == obj.user_id)
    
class IsOwnerOrStaff(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_staff or
            request.user.is_superuser or
            request.user.id == obj.user_id
        )