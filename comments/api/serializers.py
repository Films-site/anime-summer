from rest_framework import serializers
from comments.models import Comment


# class FilterCommentListSerializer(serializers.ListSerializer):
#     def to_representation(self, data):
#         data = data.filter(parent=None)
#         return super().to_representation(data)


# class RecursiveCommentSerializer(serializers.Serializer):
#     def to_representation(self, value):
#         serializer = self.parent.parent.__class__(value, context=self.context)
#         return serializer


class ChilSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text_comment = serializers.CharField(max_length=800)
    created_comment = serializers.DateTimeField()
    updated_comment = serializers.DateTimeField()


class CommnetSerializer(serializers.ModelSerializer):
    children = ChilSerializer(many=True, required=False)

    class Meta:
        # list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = (
            'id', 'text_comment', 'created_comment', 'updated_comment',
            'children',
        )
