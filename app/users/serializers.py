from app.users.models import Data
from rest_framework import serializers
from users.models import Users


class AritistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
