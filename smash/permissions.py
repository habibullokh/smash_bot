from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """
    Custom permission to check if the user is owner of the object.
    """
    message = "You can not delete another user"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # print(obj.author)
        return obj.author == request.user


class IsAdmin(BasePermission):
    """
    Custom permission to check if the user is owner of the object.
    """
    message = "You can not delete cart"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # print(obj.author)
        return request.user.is_staff or request.user.is_superuser
