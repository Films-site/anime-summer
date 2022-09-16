from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from rating.models import Rating
from rating.api.serializers import RatingSerializer
from rating.api.rating_services.rating_worker import RatingWorker


class RatingMixin:

    @action(detail=False, methods=['post'], url_path='rating')
    def create_rating(self, request, *args, **kwargs):
        appraiser = request.user
        content_id = request.data.get('content_id')
        model_for_rating = ContentType.objects.get_for_model(self.queryset.model)
        if Rating.objects.filter(appraiser=appraiser, object_id=content_id, content_type=model_for_rating).count() >= 1:
            return Response(
                {"error": "have you done this before."}, status=status.HTTP_400_BAD_REQUEST
            )

        ratung_created = Rating.objects.create(
            appraiser=appraiser, estimation=request.data.get('estimation'),
            content_type=model_for_rating, object_id=content_id,
        )
        ratings_model = Rating.objects.filter(object_id=content_id)
        model = model_for_rating.get_object_for_this_type(
            id=request.data.get('content_id')
        )
        avg_rating = RatingWorker.сalculation_average_score(ratings_model)
        model.average_rating = round(avg_rating["estimation__avg"], 1)
        model.save()
        return Response(
            RatingSerializer(
                ratung_created, context={"request": request}
            ).data, status=status.HTTP_200_OK
        )
