

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from account.managers import UserManager


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.CharField(max_length=255, default='user')
    groups_joined = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'


