from rest_framework import serializers

from users.models import Admin


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ['id', 'full_name', 'phone', 'user_name']
