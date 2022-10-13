from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Anime Summer API",
      default_version='v1',
      description='Swagger in anime-site',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Регистрация пользователей
    path('auth/', include('djoser.urls.authtoken')),
    path('api/v1/auth/', include('djoser.urls')),

    # Swagger
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('api/v1/users/', include('users.api.urls')),
    path('api/v1/anime/', include('anime.api.urls')),
    path('api/v1/comments/', include('comments.api.urls')),
    path('api/v1/rating/', include('rating.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
