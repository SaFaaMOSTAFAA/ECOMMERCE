from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Admin


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass
