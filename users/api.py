from django.contrib.auth.hashers import make_password
from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.models import Admin, CustomerAccount, Trader
from users.serializers import (AdminSerializer, CustomerAccountSerializer,
                               TraderSerializer)


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'user_name', 'phone']

    def perform_create(self, serializer):
        password = self.request.data.get('password')
        if password:
            serializer.save(password=make_password(password))
        else:
            serializer.save()

    def perform_update(self, serializer):
        password = self.request.data.get('password')
        if password:
            serializer.save(password=make_password(password))
        else:
            serializer.save()


class TraderViewSet(ModelViewSet):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

    def perform_create(self, serializer):
        password = self.request.data.get('password')
        if password:
            serializer.save(password=make_password(password))
        else:
            serializer.save()

    def perform_update(self, serializer):
        password = self.request.data.get('password')
        if password:
            serializer.save(password=make_password(password))
        else:
            serializer.save()


class CustomerAccountViewSet(ModelViewSet):
    queryset = CustomerAccount.objects.all()
    serializer_class = CustomerAccountSerializer

    def perform_create(self, serializer):
        password = self.request.data.get('password')
        if password:
            serializer.save(password=make_password(password))
        else:
            serializer.save()

    def perform_update(self, serializer):
        password = self.request.data.get('password')
        if password:
            serializer.save(password=make_password(password))
        else:
            serializer.save()


class RegisterCustomerAPIView(APIView):
    def post(self, request, format=None):
        serializer = CustomerAccountSerializer(data=request.data)
        if serializer.is_valid():
            password = self.request.data.get('password')
            if not password:
                return Response(
                    {"password": ["This field is required."]},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save(password=make_password(password))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
