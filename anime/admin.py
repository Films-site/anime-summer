from django.contrib import admin

from anime.models import (
    Anime,
    TypeAnime,
    Genre,
    RatingMPAA,
    Voiceover,
    Hero,
)


@admin.register(Anime)
class AnimeModelAdmin(admin.ModelAdmin):
    ...


@admin.register(TypeAnime)
class TypeAnimeModelAdmin(admin.ModelAdmin):
    ...


@admin.register(Genre)
class GenreModelAdmin(admin.ModelAdmin):
    ...


@admin.register(RatingMPAA)
class RatingMPAAModelAdmin(admin.ModelAdmin):
    ...


@admin.register(Voiceover)
class VoiceoverModelAdmin(admin.ModelAdmin):
    ...


@admin.register(Hero)
class HeroModelAdmin(admin.ModelAdmin):
    ...
