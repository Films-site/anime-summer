from rest_framework import serializers

from anime.models import Anime
from videos.api.serializers import VideoSerializer


class AnimeListSerializer(serializers.ModelSerializer):
    preview = serializers.SerializerMethodField()

    class Meta:
        model = Anime
        fields = ['id', 'title', 'description', 'preview']

    @staticmethod
    def get_preview(obj):
        return obj.preview


class AnimeDetailSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)

    class Meta:
        model = Anime
        fields = ['id', 'title', 'description', 'preview', 'videos']
