from rest_framework import serializers

from videos.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video', 'type', 'number_video', 'content_object']
