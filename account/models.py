

from django.contrib.auth.models import AbstractUser

from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(null=True,blank=True, unique=True, max_length=150)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.CharField(max_length=255, default='user')
    # groups_joined = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)
    # confirmation_code = models.CharField(max_length=10)

    class Meta:
        swappable = 'AUTH_USER_MODEL'


