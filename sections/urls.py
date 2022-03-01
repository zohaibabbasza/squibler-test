from django.urls import path, include
from rest_framework import routers
from sections import views

router = routers.DefaultRouter()
router.register("sections", views.SectionModelViewSet, basename="sections")

urlpatterns = [
    path("", include(router.urls)),
]
