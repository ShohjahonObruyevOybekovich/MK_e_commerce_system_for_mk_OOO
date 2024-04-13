
from django.urls import path

from .views import UserCreateAPIView, CustomAuthToken, UserUpdateAPIView

urlpatterns = [
    path('create', UserCreateAPIView.as_view(), name='user_create'),
    path('token', CustomAuthToken.as_view(), name='user_login'),
    path('user-update/<int:pk>', UserUpdateAPIView.as_view(), name='user_update'),
]
