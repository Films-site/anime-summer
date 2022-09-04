from rest_framework import serializers

from anime.models import Anime


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'description', 'preview', 'videos']
