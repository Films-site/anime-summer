from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.api.views import GoogleLogin

urlpatterns = [
    path('token-create/', TokenObtainPairView.as_view()),
    path('oauth/google/', GoogleLogin.as_view(), name='google_login')
]
