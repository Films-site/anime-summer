from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from comments.models import Comment
from comments.api.serializers import CommnetSerializer


class CommentView:

    @action(detail=False, methods=['post'], url_path='comments')
    def create_comment(self, request, *args, **kwargs):
        author = request.user
        content_id = request.data.get('content_id')
        model_for_comment = ContentType.objects.get_for_model(self.queryset.model)
        parent = request.data.get('parent')
        if parent:
            parent_comment = Comment.objects.get(id=int(parent))
            comment_created = Comment.objects.create(
                parent=parent_comment, text_comment=request.data.get('text_comment'),
                author=author, content_type=model_for_comment, object_id=content_id,
            )
        else:
            comment_created = Comment.objects.create(
                text_comment=request.data.get('text_comment'), author=author,
                content_type=model_for_comment, object_id=content_id,
            )
        return Response(
            CommnetSerializer(
                comment_created, context={"request": request}
            ).data, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['get'], url_path='comments')
    def list_comment(self, request, pk=None, *args, **kwargs):
        content_type_model = ContentType.objects.get_for_model(self.queryset.model, for_concrete_model=False)
        model = content_type_model.get_object_for_this_type(id=pk)
        if model:
            comments = model.comments.all().filter(level=0)
            return Response(
                CommnetSerializer(
                    comments, many=True, context={"request": request}
                ).data, status=status.HTTP_200_OK
            )
        else:
            return Response({
                "error": "error"
            }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='comments')
    def update_comment(self, request, pk=None):
        if not Comment.objects.filter(author=request.user.id, id=pk).exists():
            return Response(
                {"error": "This is not your comment"}, status=status.HTTP_400_BAD_REQUEST
            )

        comment_obj = Comment.objects.get(author=request.user.id, id=pk)
        comment_obj.text_comment = request.data.get('new_text_comment')
        comment_obj.save()
        return Response(
            CommnetSerializer(
                comment_obj, context={"request": request}
            ).data, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['delete'], url_path='comments')
    def destroy_comment(self, request, pk=None):
        if Comment.objects.get(author=request.user.id, id=pk):
            comment_obj = Comment.objects.get(author=request.user.id, id=pk)
            comment_obj.delete()
            return Response(
                {"result": "Deleted"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "This is not your comment"}, status=status.HTTP_400_BAD_REQUEST
            )
