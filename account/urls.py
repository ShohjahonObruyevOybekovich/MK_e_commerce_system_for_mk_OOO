
from django.urls import path

from .views import UserCreateAPIView, CustomAuthToken, UserUpdateAPIView,ListUserAPIView

urlpatterns = [
    path('create', UserCreateAPIView.as_view(), name='user_create'),
    path('token', CustomAuthToken.as_view(), name='user_login'),
    path('user-list',ListUserAPIView.as_view(), name='user_list'),
    path('user-update/<int:pk>', UserUpdateAPIView.as_view(), name='user_update'),
]
