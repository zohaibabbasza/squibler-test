from rest_framework import permissions
from mp_nodes import models


class UserDeletePermissionTree(permissions.BasePermission):
    def has_permission(self, request, view):
        user = models.TreeSection.objects.get(id=view.kwargs["pk"]).owner
        if view.action in ["destroy"] and user.id != request.user.id:
            return False
        return True
