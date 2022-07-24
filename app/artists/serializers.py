from rest_framework import serializers
from artists.models import Artist


class AritistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name')
