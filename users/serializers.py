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


class TraderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trader
        fields = [
            'id', 'full_name', 'email', 'phone', 'user_name',
            'is_active', 'address', 'password', 'created', 'modified']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }


class CustomerAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAccount
        fields = [
            'id', 'full_name', 'email', 'phone', 'user_name',
            'is_active', 'address', 'email', 'password', 'created', 'modified']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }


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
        token = super().get_token(user)
        token['role'] = user.get_role()
        token['name'] = user.full_name
        return token
