from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from loguru import logger
from zoo.models import Animals, Profile, Aviary
from zoo.serializers import AnimalsSerializer, UserSerializer, GroupSerializer, ProfileSerializer, AviarySerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animals.objects.select_related('aviaryID').all()
    serializer_class = AnimalsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.select_related('profile').prefetch_related('groups').all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class AviaryViewSet(viewsets.ModelViewSet):
    queryset = Aviary.objects.all()
    serializer_class = AviarySerializer

