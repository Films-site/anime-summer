from rest_framework import serializers

from rating.models import Rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = [
            'id', 'appraiser', 'estimation',
        ]
