import logging

from rest_framework import permissions

from .models import User


class IsOwnerOrReadOnlyUserModel(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it. (and others to read)
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.auth_user == request.user

class IsOwnerOrReadOnlyWithAuthorModel(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it. (and others to read)
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.author.auth_user == request.user

#User.objects.get(pk=obj.author).auth_user_id == request.user.auth_user_id