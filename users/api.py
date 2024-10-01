from datetime import timedelta

from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone
from rest_framework import filters, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.models import (Admin, CustomerAccount, PasswordReset, Trader,
                          UserAccount)
from users.permissions import IsAdmin
from users.serializers import (AdminSerializer, CustomerAccountSerializer,
                               ResetPasswordRequestSerializer,
                               ResetPasswordSerializer, TraderSerializer)


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.order_by('-id')
    serializer_class = AdminSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'user_name', 'phone']


class TraderViewSet(ModelViewSet):
    queryset = Trader.objects.order_by('-id')
    serializer_class = TraderSerializer
    permission_classes = [IsAdmin]


class CustomerAccountViewSet(ModelViewSet):
    queryset = CustomerAccount.objects.order_by('-id')
    serializer_class = CustomerAccountSerializer


class RegisterCustomerAPIView(APIView):
    def post(self, request, format=None):
        serializer = CustomerAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = request.data.get('password')
        serializer.save(password=make_password(password))

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RequestPasswordReset(generics.GenericAPIView):
    permission_classes = ()
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):

        email = request.data['email']
        user = UserAccount.objects.filter(email__iexact=email).first()

        if user:
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            expiration_date = timezone.now() + timedelta(hours=1)

            reset = PasswordReset.objects.create(  # noqa
                email=email, token=token, expiration_date=expiration_date)
            return Response({'success': token}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User with credentials not found"},
                            status=status.HTTP_404_NOT_FOUND)


class ResetPassword(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = []

    def post(self, request, token):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        new_password = data['new_password']
        confirm_password = data['confirm_password']

        if new_password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=400)

        reset_obj = PasswordReset.objects.filter(token=token).first()

        if not reset_obj:
            return Response({'error': 'Invalid token'}, status=400)

        user = UserAccount.objects.filter(email=reset_obj.email).first()

        if user:
            user.set_password(request.data['new_password'])
            user.save()
            reset_obj.delete()

            return Response({'success': 'Password updated'})
        else:
            return Response({'error': 'No user found'}, status=404)
