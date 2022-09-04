from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Video:
    ANIME_SERIES = 'anime_series'
    TYPE_VIDEO = (
        (ANIME_SERIES, 'Серия аниме'),
    )

    video = models.FileField('Видео')
    type = models.TextField('Тип видео', choices=TYPE_VIDEO)
    number_video = models.PositiveIntegerField('Номер серии', blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
