from django_filters import rest_framework as filters

from anime.models import Anime


class AnimeFilter(filters.FilterSet):
    class Meta:
        model = Anime
        fields = ['title', 'description']
