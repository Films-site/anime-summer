from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from videos.models import Video


class Anime(models.Model):
    title = models.TextField('Название')
    description = models.TextField('Описание')
    preview = ProcessedImageField(
        format='JPEG',
        processors=[
            ResizeToFill(250, 350)
        ],
        verbose_name='Превью для аниме',
    )
    videos = GenericRelation(Video)
