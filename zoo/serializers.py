from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Animals, Profile, Aviary
from loguru import logger


class AviarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aviary
        fields = ['id','number']

class AnimalsSerializer(serializers.ModelSerializer):
    aviary_info = AviarySerializer(source='aviaryID', read_only=True)
    class Meta:
        model = Animals
        fields = ['id', 'name', 'age', 'weight', 'photoPath', 'aviary_info']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['age', 'bio']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class UserSerializer(serializers.ModelSerializer):
    profile_info = ProfileSerializer(source='profile', read_only=True)
    group_info = GroupSerializer(source='groups', many=True, read_only=True)
    class Meta:
        model = User
        fields = ["url", "username", "email", "group_info", "profile_info"]
