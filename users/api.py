from django.contrib.auth.hashers import make_password
from rest_framework import filters
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
