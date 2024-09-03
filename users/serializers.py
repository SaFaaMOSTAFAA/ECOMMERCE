from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Admin, CustomerAccount, Trader


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ['id', 'full_name',
                  'phone', 'user_name', 'is_active', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }


class TraderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trader
        fields = [
            'id', 'full_name',
            'phone', 'user_name', 'is_active', 'address', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }


class CustomerAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAccount
        fields = [
            'id', 'full_name',
            'phone', 'user_name', 'is_active', 'address', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass
