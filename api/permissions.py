from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to have access and edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
