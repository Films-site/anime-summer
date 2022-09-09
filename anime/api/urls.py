from rest_framework import routers
from django.urls import path

from anime.api.views import AnimeModelViewSet


router = routers.DefaultRouter()
router.register('', AnimeModelViewSet)

urlpatterns = [
    path('add-comment/', AnimeModelViewSet.as_view({'post': 'create'}))
]
urlpatterns += router.urls
