from django.contrib.auth.models import AbstractUser
from django.db import models

from account.managers import UserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=11, unique=True)
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    USERNAME_FIELD = 'username'
    objects = UserManager()
    class Meta:
        swappable = 'AUTH_USER_MODEL'

