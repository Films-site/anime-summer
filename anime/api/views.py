from elasticsearch_dsl import Q
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from anime.api.filters import AnimeFilter
from anime.api.serializers import AnimeListSerializer
from anime.documents import AnimeDocument
from anime.models import Anime
from plans.api.views import PlanMixin
from search.api.views import PaginatedElasticSearchAPIView


class AnimeModelViewSet(PaginatedElasticSearchAPIView, PlanMixin, ModelViewSet):
    queryset = Anime.objects.all()

    document_class = AnimeDocument

    default_permissions_classes = AllowAny
    default_serializer_class = AnimeListSerializer

    permissions_classes = {
        'create': IsAdminUser,
    }
    serializer_classes = {
        'list': AnimeListSerializer,
    }

    filterset_class = AnimeFilter

    def get_permissions(self):
        self.permission_classes = [self.permissions_classes.get(self.action,
                                                                self.default_permissions_classes)]
        return super().get_permissions()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)

    def generate_q_expression(self, query):
        return Q('multi_match',
                 query=query,
                 fields=['title'],
                 minimum_should_match=1,
                 fuzziness='auto')
