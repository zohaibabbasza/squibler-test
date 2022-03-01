from django.urls import path, include
from rest_framework import routers
from mp_nodes import views

router = routers.DefaultRouter()
router.register("tree-sections", views.TreeSectionModelViewSet, basename="sections")

urlpatterns = [
    path("", include(router.urls)),
]
