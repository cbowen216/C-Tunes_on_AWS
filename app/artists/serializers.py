from app.artists.models import Data
from rest_framework import serializers
from artists.models import Tutorial


class AritistSerializer(serializers.ModelSerializer):
    class Meta:
        model = artist
        fields = ('id', 'title', 'tutorial_url', 'image_path', 'description',
                  'published')
