from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

User = get_user_model()


class PlanItem(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Предмет плана'
        verbose_name_plural = 'Предметы в планах'
        unique_together = ('content_type', 'object_id')


class Plan(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    items = models.ManyToManyField(PlanItem, related_name='items', blank=True)

    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'

    def __str__(self):
        return self.user.email
