from django.contrib import admin

from anime.models import Anime


@admin.register(Anime)
class AnimeModelAdmin(admin.ModelAdmin):
    ...
