from decimal import Decimal

import uuid
from django.db import models
from django.db.models import UniqueConstraint
from django.utils import timezone
from account.models import CustomUser
import json

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)


# class Product(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     product_comment = models.CharField(max_length=255, null=True, blank=True)
#     product_owner = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)
#     photos_or_videos = models.ManyToManyField('ProductMedia', related_name='products')
#     is_top = models.BooleanField(default=False)
#
#     def save(self, *args, **kwargs):
#         self.updated_at = timezone.now()
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_comment = models.CharField(max_length=255, null=True, blank=True)
    product_owner = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    photos_or_videos = models.ManyToManyField('ProductMedia')

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProductMedia(models.Model):
    file = models.FileField(upload_to='media/product_media/')
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"

class Payment(models.Model):
    payment_type = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    currency = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class PurchaseHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total_amount = Decimal(self.price) * self.product_amount
        super().save(*args, **kwargs)

class Savatcha(models.Model):
    uuid = models.UUIDField(unique=True,default=uuid.uuid4(), editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_amount = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class liked(models.Model):
    uuid = models.UUIDField(unique=True,default=uuid.uuid4(), editable=False)
    # id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product'], name='liked_product')
        ]

    def __str__(self):
        return f"{self.user} liked {self.product}"


# class Comments(models.Model):
#     id = models.IntegerField(primary_key=True)
#     text = models.TextField()
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     comment_to_product = models.ForeignKey(Product, on_delete=models.CASCADE)

from django.db import models

class Versions(models.Model):
    id = models.AutoField(primary_key=True)
    version_new = models.CharField(max_length=255)
    version_last = models.CharField(max_length=255, default=" ",null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        # Check if the instance already exists in the database
        if self.pk:
            # Fetch the current instance from the database
            current_instance = Versions.objects.get(pk=self.pk)
            # Update version_last with the current version_new before saving
            self.version_last = current_instance.version_new
        super(Versions, self).save(*args, **kwargs)

    def __str__(self):
        return f"New Version: {self.version_new}, Last Version: {self.version_last}"
