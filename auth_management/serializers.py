from rest_framework import serializers

from auth_management.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)
