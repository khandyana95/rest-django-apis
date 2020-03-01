from rest_framework import permissions


class UpdateOwnUserProfile(permissions.BasePermission):
    """Adding object level permission to User for profile"""

    def has_object_permission(self, request, view, obj):
        """restricting object permissions"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnUserProfileFeed(permissions.BasePermission):
    """Adding Object level permission to profile feed"""

    def has_object_permission(self, request, view, obj):
        """Restricting the Object Permissions"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id == request.user.id
