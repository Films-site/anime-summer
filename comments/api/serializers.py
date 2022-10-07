from rest_framework import serializers
from comments.models import Comment
from users.api.serializers import UserSerializer


class ChildrenSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text_comment = serializers.CharField(max_length=800)
    created_comment = serializers.DateTimeField()
    updated_comment = serializers.DateTimeField()
    author = UserSerializer(required=False,)


class CommnetSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False,)
    children = ChildrenSerializer(many=True, required=False)

    class Meta:
        model = Comment
        fields = (
            'id', 'text_comment', 'created_comment', 'updated_comment',
            'author', 'children',
        )
