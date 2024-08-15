from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from users.models import Admin
from users.serializers import AdminSerializer


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def perform_create(self, serializer):
        phone = self.request.data.get('phone')
        if not phone.isdigit():
            raise ValidationError(
                {"phone": "Phone number must contain only digits."})
        serializer.save()

    def perform_update(self, serializer):
        phone = self.request.data.get('phone')
        if not phone.isdigit():
            raise ValidationError(
                {"phone": "Phone number must contain only digits."})
        serializer.save()
