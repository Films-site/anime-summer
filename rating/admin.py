from django.contrib import admin

from rating.models import Rating


@admin.register(Rating)
class RatingModelAdmin(admin.ModelAdmin):
    ...
