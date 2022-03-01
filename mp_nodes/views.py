from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from mp_nodes import models, serializers
from .permissions import UserDeletePermissionTree


class TreeSectionModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    serializer_class = serializers.TreeSectionSerializer

    def get_queryset(self):
        return models.TreeSection.objects.filter(
            Q(collaboration__id__in=[self.request.user.id]) | Q(owner=self.request.user)
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.request.method in ["DELETE"]:
            return [UserDeletePermissionTree()]
        else:
            return [IsAuthenticated()]

    @action(detail=False, url_path="add-collaborator", methods=["post"])
    def add_or_remove_collaborator(self, request):
        try:
            email = request.data["email"]
            section = models.TreeSection.objects.filter(id=request.data["section_id"])
            user = models.User.objects.filter(email=email)
            if section.exists() and user.exists():
                section = section.first()
                user = user.first()
                if section.owner != request.user:
                    return Response(
                        {"msg": "You don't have permission to perform this task"},
                        status=status.HTTP_200_OK,
                    )
                if user in section.collaboration.all():
                    section.collaboration.remove(user)
                    return Response(
                        {"msg": "User Removed Added"}, status=status.HTTP_200_OK
                    )
                else:
                    section.collaboration.add(user)
                return Response(
                    {"msg": "User Successfully Added"}, status=status.HTTP_200_OK
                )
            return Response(
                {"msg": "No user or section found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({"error": e}, status=status.HTTP_404_NOT_FOUND)
