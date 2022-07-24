from rest_framework import serializers
from artists.models import Artist


class AritistSerializer(serializers.ModelSerializer):
    class Meta:
        model = artist
        fields = ('id', 'title', 'tutorial_url', 'image_path', 'description',
                  'published')
