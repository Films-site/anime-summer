from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from videos.models import Video
from comments.models import Comment


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
    comments = GenericRelation(Comment, related_name='anime_comments')

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'
