from rest_framework import routers

from comments.api.views import CommentView


router = routers.DefaultRouter()
router.register('', CommentView)

urlpatterns = []
urlpatterns += router.urls
