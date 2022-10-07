from rest_framework import routers
# from django.urls import path

from anime.api.views import AnimeModelViewSet


router = routers.DefaultRouter()
router.register('', AnimeModelViewSet)

urlpatterns = []
urlpatterns += router.urls
