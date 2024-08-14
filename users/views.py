from rest_framework.viewsets import ModelViewSet

from users.models import Admin
from users.serializers import AdminSerializer


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
