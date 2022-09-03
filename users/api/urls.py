from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('token-create/', TokenObtainPairView.as_view()),
]
