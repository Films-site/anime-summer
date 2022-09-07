from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes

from anime.models import Anime
from comments.models import Comment

from comments.api.serializers import CommnetSerializer


class Comment(viewsets.ViewSet):
    queryset = Comment.objects.all()

    @permission_classes([IsAuthenticated])
    def create(self, request, *args, **kwargs):
        author = request.user
        if request.data.get('parent'):
            parent = request.data.get('parent')
            parent_comment = Comment.objects.get(id=int(parent))
            content_id = request.data.get('content_id')
            anime = ContentType.objects.get_for_model(Anime)
            text = request.data.get('text_comment')
            Comment.objects.create(
                parent=parent_comment, text_comment=text, author=author,
                content_type=anime, object_id=content_id,
            )
        else:
            content_id = request.data.get('content_id')
            anime = ContentType.objects.get_for_model(Anime)
            text = request.data.get('text_comment')
            Comment.objects.create(
                text_comment=text, author=author,
                content_type=anime, object_id=content_id,
            )

        return Response({
            "Comment created": "ok"
        }, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        anime_id = request.data.get('anime_id')
        # try:
        if Anime.objects.get(id=anime_id):
            anime_obj = Anime.objects.get(id=anime_id)
            print(anime_obj)
            comments = anime_obj.comments.all().filter(level=0)
            print(comments)
            return Response(
                CommnetSerializer(
                    comments, many=True, context={"request": request}
                ).data,
            )
        else:
            return Response({
                "test": 'error'
            }, status=status.HTTP_400_BAD_REQUEST)
        # except Exception:
        #     return Response({
        #         "test": 'error'
        #     }, status=status.HTTP_400_BAD_REQUEST)
