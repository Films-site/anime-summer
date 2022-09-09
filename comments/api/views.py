from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework import status

from anime.models import Anime
from comments.models import Comment
from comments.api.serializers import CommnetSerializer


class CommentCreate:

    def create(self, request, *args, **kwargs):
        author = request.user
        content_id = request.data.get('content_id')
        anime = ContentType.objects.get_for_model(self.queryset.model)
        text = request.data.get('text_comment')
        if request.data.get('parent'):
            parent = request.data.get('parent')
            parent_comment = Comment.objects.get(id=int(parent))
            Comment.objects.create(
                parent=parent_comment, text_comment=text, author=author,
                content_type=anime, object_id=content_id,
            )
        else:
            Comment.objects.create(
                text_comment=text, author=author,
                content_type=anime, object_id=content_id,
            )
        return Response({
            "Comment created": "ok"
        }, status=status.HTTP_201_CREATED)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, *args, **kwargs):
        anime_id = request.data.get('anime_id')
        if Anime.objects.get(id=anime_id):
            anime_obj = Anime.objects.get(id=anime_id)
            comments = anime_obj.comments.all().filter(level=0)
            return Response(
                CommnetSerializer(
                    comments, many=True, context={"request": request}
                ).data, status=status.HTTP_200_OK
            )
        else:
            return Response({
                "error": "error"
            }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if not Comment.objects.filter(author=request.user.id, id=pk).exists():
            return Response(
                {"error": "Это не ваш комментарий"}, status=status.HTTP_400_BAD_REQUEST
            )
        comment_obj = Comment.objects.get(author=request.user.id, id=pk)
        comment_obj.text_comment = request.data.get('new_text_comment')
        comment_obj.save()
        return Response(
            CommnetSerializer(
                comment_obj, context={"request": request}
            ).data, status=status.HTTP_200_OK
        )

    def destroy(self, request, pk=None):
        if Comment.objects.get(author=request.user.id, id=pk):
            comment_obj = Comment.objects.get(author=request.user.id, id=pk)
            comment_obj.delete()
            return Response(
                {"result": "Deleted"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Это не ваш комментарий"}, status=status.HTTP_400_BAD_REQUEST
            )
