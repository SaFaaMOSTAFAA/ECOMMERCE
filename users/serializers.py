from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Admin, CustomerAccount, PasswordReset, Trader


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ['id', 'full_name', 'email', 'phone',
                  'user_name', 'is_active', 'password', 'created', 'modified']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

        def validate_password(self, value):
            return make_password(value)

        def create(self, validated_data):
            instance = super().create(validated_data)
            return instance

        def update(self, instance, validated_data):
            password = validated_data['password']
            if password:
                instance.password = make_password(password)
            instance.save()
            return instance


class TraderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trader
        fields = [
            'id', 'full_name', 'email', 'phone', 'user_name',
            'is_active', 'address', 'password', 'created', 'modified']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

        def validate_password(self, value):
            return make_password(value)

        def create(self, validated_data):
            instance = super().create(validated_data)
            return instance

        def update(self, instance, validated_data):
            password = validated_data['password']
            if password:
                instance.password = make_password(password)
            instance.save()
            return instance


class CustomerAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAccount
        fields = [
            'id', 'full_name', 'email', 'phone', 'user_name',
            'is_active', 'address', 'email', 'password', 'created', 'modified']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

        def validate_password(self, value):
            return make_password(value)

        def create(self, validated_data):
            instance = super().create(validated_data)
            return instance

        def update(self, instance, validated_data):
            password = validated_data['password']
            if password:
                instance.password = make_password(password)
            instance.save()
            return instance


class ResetPasswordRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PasswordReset
        fields = ['email']


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.RegexField(
        regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        write_only=True,
        error_messages={
            'invalid': (
                'Password must be at least 8 characters long with '
                'at least one capital letter and symbol'
            )
        }
    )
    confirm_password = serializers.CharField(write_only=True, required=True)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        data = super().get_token(user)
        data['role'] = user.get_role()
        data['email'] = user.email
        return data
