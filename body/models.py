from decimal import Decimal

from django.db import models
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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_amount = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class liked(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


# class Comments(models.Model):
#     id = models.IntegerField(primary_key=True)
#     text = models.TextField()
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     comment_to_product = models.ForeignKey(Product, on_delete=models.CASCADE)