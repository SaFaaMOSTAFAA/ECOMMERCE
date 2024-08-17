from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet

from users.models import Admin
from users.serializers import AdminSerializer


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

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