from rest_framework import permissions
from sections import models


class UserDeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = models.Section.objects.get(id=view.kwargs["pk"]).owner
        if view.action in ["destroy"] and user.id != request.user.id:
            return False
        return True
