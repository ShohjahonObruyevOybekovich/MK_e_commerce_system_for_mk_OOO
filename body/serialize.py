from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product, PurchaseHistory, Savatcha, Category, liked, Payment

User = get_user_model()


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'  # Assuming Payment model has fields to be serialized


class ProductCreateSerializer(serializers.ModelSerializer):
    product_owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    payment = PaymentSerializer()

    class Meta:
        model = Product
        fields = ['name', 'photo_or_video', 'price', 'product_comment', 'product_owner', 'payment']
        read_only_fields = ['created_at']


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'photo_or_video', 'price', 'product_comment']
        read_only_fields = ['created_at', 'product_owner']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'photo_or_video', 'price', 'product_comment', 'created_at']
        read_only_fields = ['name', 'photo_or_video', 'price', 'product_comment', 'created_at']


class PurchaseHistorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    product = ProductListSerializer()
    total_amount = serializers.DecimalField(max_digits=10,
                                            decimal_places=2)  # Assuming this field exists in PurchaseHistory model

    class Meta:
        model = PurchaseHistory
        fields = ['product_amount', 'price', 'user', 'product', 'total_amount']
        read_only_fields = ['created_at']


class SavatchaCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    product = ProductListSerializer()

    class Meta:
        model = Savatcha
        fields = ['user', 'product']
        read_only_fields = ['created_at']


class SavatchaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savatcha
        fields = ['user', 'product']
        read_only_fields = ['created_at']


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'type']
        read_only_fields = ['created_at']


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'type']
        read_only_fields = ['created_at']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'type']
        read_only_fields = ['created_at']


class LikedProductCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    product = ProductListSerializer()

    class Meta:
        model = liked
        fields = ['user', 'product']
        read_only_fields = ['created_at']
