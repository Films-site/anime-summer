from rest_framework import serializers

from anime.models import Anime
from videos.api.serializers import VideoSerializer


class AnimeSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)

    class Meta:
        model = Anime
        fields = ['id', 'title', 'description', 'preview', 'videos']
