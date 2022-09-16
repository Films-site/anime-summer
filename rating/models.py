from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth import get_user_model


class Rating(models.Model):
    appraiser = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        verbose_name='Оценивший пользователь',
        related_name='appraiser_user',
    )
    estimation = models.PositiveIntegerField(
        verbose_name='Оценка',
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{str(self.appraiser)} {str(self.object_id)}'

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
