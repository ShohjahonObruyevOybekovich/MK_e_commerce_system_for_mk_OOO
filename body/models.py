import datetime
from decimal import Decimal

from django.db import models
from django.utils import timezone


class User(models.Model):

    id = models.IntegerField(primary_key=True)
    photo = models.ImageField(upload_to='Account_photos/', null=True, blank=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)
    groups_joined = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(datetime.date)
    updated_at = models.DateField(datetime.date)

class Category(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    created_at = models.DateField(datetime.date)
    updated_at = models.DateField(datetime.date)


class Product(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField is generally preferred over IntegerField for primary keys
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', null=True ,blank=True,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Better suited for representing prices
    product_comment = models.CharField(max_length=255, null=True, blank=True)
    product_owner = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL)
    payment = models.ForeignKey('Payment', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)  # Use DateTimeField for creation and update timestamps
    updated_at = models.DateTimeField(default=timezone.now)
    photo_or_video = models.ImageField(upload_to='product_photos/', null=True, blank=True)  # Use ImageField for photos

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()  # Update the timestamp whenever the object is saved
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Payment(models.Model):
    payment_type = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    currency = models.CharField(max_length=255)
    created_at = models.DateField(datetime.date)
    updated_at = models.DateField(datetime.date)


class PurchaseHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    product_amount = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Changed to DecimalField for price
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False, blank=True)  # Changed to DecimalField for total_amount
    created_at = models.DateField(default=timezone.now)  # Changed to DateField for consistency
    updated_at = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Calculate total amount before saving
        self.total_amount = Decimal(self.price) * self.product_amount
        super().save(*args, **kwargs)


class Savatcha(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateField(datetime.date)
    updated_at = models.DateField(datetime.date)

class liked(models.Model):

    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateField(datetime.date)
    updated_at = models.DateField(datetime.date)
