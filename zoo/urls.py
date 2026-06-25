from django.urls import path, include
from zoo import views
from rest_framework import routers

from zoo.views import AnimalViewSet

router = routers.DefaultRouter()
router.register(r'animals', views.AnimalViewSet)