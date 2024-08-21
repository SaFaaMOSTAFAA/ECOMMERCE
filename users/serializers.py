from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Admin


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ['id', 'full_name', 'phone', 'user_name', 'is_active']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass
