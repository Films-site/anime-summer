from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from anime.api.filters import AnimeFilter
from anime.api.serializers import AnimeSerializer
from anime.models import Anime


class AnimeModelViewSet(ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

    default_permissions_classes = AllowAny

    permissions_classes = {
        'create': IsAdminUser,
    }

    filterset_class = AnimeFilter

    def get_permissions(self):
        self.permission_classes = [self.permissions_classes.get(self.action,
                                                                self.default_permissions_classes)]
        return super().get_permissions()
