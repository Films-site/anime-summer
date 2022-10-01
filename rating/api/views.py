from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from rating.models import Rating
from rating.api.serializers import RatingSerializer
from rating.api.rating_services.service import RatingCalculation


class RatingMixin:

    @action(detail=False, methods=['post'], url_path='rating')
    def create_rating(self, request, *args, **kwargs):
        appraiser = request.user
        content_id = request.data.get('content_id')
        model_for_rating = ContentType.objects.get_for_model(self.queryset.model)
        if Rating.objects.filter(appraiser=appraiser, object_id=content_id, content_type=model_for_rating).count() >= 1:
            return Response(
                {"error": "Have you done this before"}, status=status.HTTP_400_BAD_REQUEST
            )

        ratung_created = Rating.objects.create(
            appraiser=appraiser, estimation=request.data.get('estimation'),
            content_type=model_for_rating, object_id=content_id,
        )
        ratings_model = Rating.objects.filter(object_id=content_id)
        model = model_for_rating.get_object_for_this_type(
            id=request.data.get('content_id')
        )
        avg_rating = RatingCalculation.сalculation_average_score(ratings_model)
        model.average_rating = round(avg_rating["estimation__avg"], 1)
        model.save()
        return Response(
            RatingSerializer(
                ratung_created, context={"request": request}
            ).data, status=status.HTTP_201_CREATED
        )

    @create_rating.mapping.put
    def update_rating(self, request):
        appraiser = request.user
        rating_id = request.data.get('rating_id')
        new_rating = request.data.get('new_rating')
        content_id = request.data.get('content_id')
        model_for_rating = ContentType.objects.get_for_model(self.queryset.model)
        rating_user = Rating.objects.get(id=rating_id, appraiser=appraiser, content_type=model_for_rating)
        if not rating_user:
            return Response(
                {"error": "You can't change not your grade or there is no such grade"}
            )

        rating_user.estimation = new_rating
        rating_user.save()
        ratings_model = Rating.objects.filter(object_id=content_id)
        avg_rating = RatingCalculation.сalculation_average_score(ratings_model)
        model = model_for_rating.get_object_for_this_type(
            id=content_id
        )
        model.average_rating = round(avg_rating["estimation__avg"], 1)
        model.save()
        return Response(
            RatingSerializer(
                rating_user, context={"request": request}
            ).data, status=status.HTTP_201_CREATED
        )

    @create_rating.mapping.delete
    def delete_rating(self, request):
        appraiser = request.user
        rating_id = request.data.get('rating_id')
        content_id = request.data.get('content_id')
        model_for_rating = ContentType.objects.get_for_model(self.queryset.model)
        rating_user = Rating.objects.filter(id=rating_id, appraiser=appraiser, content_type=model_for_rating)
        if not rating_user:
            return Response(
                {"error": "You can't change not your grade or there is no such grade"}
            )

        rating_user.delete()
        ratings_model = Rating.objects.filter(object_id=content_id)
        avg_rating = RatingCalculation.сalculation_average_score(ratings_model)
        model = model_for_rating.get_object_for_this_type(
            id=content_id
        )
        if avg_rating:
            model.average_rating = round(avg_rating["estimation__avg"], 1)
            model.save()
            return Response(
                {"result": "Deleted"}
            )
        model.average_rating = float(0.0)
        model.save()
        return Response(
            {"result": "Deleted"}
        )
