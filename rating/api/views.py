from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.db.models import Avg

from rating.models import Rating


class RatingMixin:

    @action(detail=False, methods=['post'], url_path='rating')
    def create_rating(self, request, *args, **kwargs):
        appraiser = request.user
        content_id = request.data.get('content_id')
        model_for_rating = ContentType.objects.get_for_model(self.queryset.model)
        if len(Rating.objects.filter(appraiser=appraiser, object_id=content_id, content_type=model_for_rating)) >= 1:
            return Response(
                {"ERROR": "have you done this before"}, status=status.HTTP_400_BAD_REQUEST
            )

        Rating.objects.create(
            appraiser=appraiser, estimation=request.data.get('estimation'),
            content_type=model_for_rating, object_id=content_id,
        )
        ratings_model = Rating.objects.filter(object_id=content_id)
        model = model_for_rating.get_object_for_this_type(
            id=request.data.get('content_id')
        )
        avg_rating = self.сalculation_average_score(ratings_model)
        model.average_rating = round(avg_rating["estimation__avg"], 1)
        model.save()
        return Response(
            {"Status": "OK"}, status=status.HTTP_201_CREATED
        )

    def сalculation_average_score(self, ratings_model):
        average_score = ratings_model.values_list(
            'estimation', flat=True
        ).aggregate(Avg('estimation'))
        return average_score
