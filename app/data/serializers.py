from app.data.models import Data
from rest_framework import serializers
from tutorials.models import Tutorial


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'title', 'tutorial_url', 'image_path', 'description',
                  'published')
