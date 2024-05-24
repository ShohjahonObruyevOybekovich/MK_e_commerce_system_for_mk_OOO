

from django.contrib.auth.models import AbstractUser

from django.db import models

from account.managers import UserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, blank=True, unique=True)
    image = models.ImageField(upload_to='media/profile_pics/', null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.CharField(max_length=255, default='user')
    telegram_username = models.CharField(max_length=255, null=True, blank=True,unique=True)
    # groups_joined = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)
    # confirmation_code = models.CharField(max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = UserManager()

    # class Meta:
    #     swappable = 'AUTH_USER_MODEL'


