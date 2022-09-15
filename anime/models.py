from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from videos.models import Video
from comments.models import Comment


class Anime(models.Model):

    STATUS_ANIME = [
        ('Онгоинг', 'Выходит последний сезон аниме'),
        ('Вышел', 'Аниме вышло.'),
        ('Анонс', 'Аниме анонсированно'),
    ]

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

    type_anime = models.ForeignKey(
        'TypeAnime', verbose_name='Тип',
        on_delete=models.PROTECT,
        related_name='type_anime',
    )
    genres_anime = models.ManyToManyField(
        'Genre', verbose_name='Жанр',
        on_delete=models.PROTECT,
        related_name='genres_anime',
    )
    next_episode = models.CharField(
        verbose_name='Следующий эпизод',
        max_length=255,
    )
    episode_anime = models.CharField(
        verbose_name='Количество эпизодов',
        max_length=255,
    )
    status_anime = models.CharField(
        verbose_name='Статус аниме',
        choices=STATUS_ANIME,
        default='Анонс',
        max_length=255,
    )
    original_source = models.CharField(
        verbose_name='Первоисточник',
        max_length=255,
    )
    season_anime = models.CharField(
        verbose_name='Сезон',
        max_length=255,
    )
    release_anime = models.CharField(
        verbose_name='Выпуск',
        max_length=255,
    )
    atelier_anime = models.CharField(
        verbose_name='Студия',
        max_length=255,
    )
    duration_series = models.CharField(
        verbose_name='Длительность',
        max_length=255,
    )
    rating_mpaa = models.ForeignKey(
        'RatingMPAA',
        verbose_name='Рейтинг-MPAA',
        related_name='rating_mpaa',
        null=True,
        blank=True,
    )
    age_rating = models.CharField(
        verbose_name='Возрастной рейтинг',
        max_length=15,
    )
    voiceovers_amine = models.ManyToManyField(
        'Voiceover', verbose_name='Озвучка',
        on_delete=models.PROTECT,
        related_name='voiceovers_anime',
    )
    main_heroes = models.ManyToMany(
        'Hero', verbose_name='Герои',
        on_delete=models.PROTECT,
        related_name='main_heroes',
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'


class TypeAnime(models.Model):
    type_content = models.CharField(
        verbose_name='Тип',
        max_length=255,
    )

    def __str__(self):
        return self.type_content

    class Meta:
        verbose_name = 'Type anime'
        verbose_name_plural = 'Types anime'


class Genre(models.Model):
    genre = models.CharField(
        verbose_name='Жанр',
        max_length=255,
    )

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class RatingMPAA(models.Model):
    rating = models.CharField(
        verbose_name='Рейтинг-MPAA',
        max_length=255,
    )

    def __str__(self):
        return self.rating

    class Meta:
        verbose_name = 'RatingMPAA'
        verbose_name_plural = 'RatingMPAA'


class Voiceover(models.Model):
    voiceover = models.CharField(
        verbose_name='Озвучка',
        max_length=255,
    )

    def __str__(self):
        return self.voiceover

    class Meta:
        verbose_name = 'Voiceover'
        verbose_name_plural = 'Voiceovers'


class Hero(models.Model):
    hero = models.CharField(
        verbose_name='Герой',
        max_length=255,
    )

    def __str__(self):
        return self.hero

    class Meta:
        verbose_name = 'Hero'
        verbose_name_plural = 'Heroes'
