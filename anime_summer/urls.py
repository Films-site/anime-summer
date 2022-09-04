from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Регистрация пользователей
    path('auth/', include('djoser.urls')),

    path('api/v1/users/', include('users.api.urls')),
    path('api/v1/anime/', include('anime.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
