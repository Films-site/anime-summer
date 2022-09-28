from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from mptt.models import MPTTModel, TreeForeignKey


class Comment(MPTTModel):
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    text_comment = models.TextField('Текст комментария')
    author = models.ForeignKey(
        'users.User', on_delete=models.CASCADE,
        verbose_name='Автор комментария',
        related_name='author_user',
    )
    created_comment = models.DateTimeField(
        'Дата написания', auto_now_add=True, blank=True
    )
    updated_comment = models.DateTimeField('Дата обновления', auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return str(f"{self.author} {self.id}")

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
