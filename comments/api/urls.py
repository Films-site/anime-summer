from rest_framework import routers

from comments.api.views import Comment


router = routers.DefaultRouter()
router.register('', Comment)

urlpatterns = []
urlpatterns += router.urls
