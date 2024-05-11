from rest_framework import request

from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth import get_user_model

from account.serializers import UserSerializer
from .models import Product, PurchaseHistory, Savatcha, Category, liked, Payment, ProductMedia

User = get_user_model()

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
        fields = ['id', 'name', 'type', 'created_at']
        read_only_fields = ['id', 'created_at']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    product_owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    # payment = PaymentSerializer()

    class Meta:
        model = Product
        fields = ['name', 'photos_or_videos','category','price', 'product_comment', 'product_owner']
        read_only_fields = ['created_at']


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'photos_or_videos', 'price', 'product_comment']
        read_only_fields = ['created_at', 'product_owner']

class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    photos_or_videos = ProductMediaSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','product_owner', 'photos_or_videos','category' ,'price', 'product_comment']
        read_only_fields = ['created_at']
class ProductListforSavatchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']
        read_only_fields = ['created_at']

class PurchaseHistoryCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()  # Field for user ID
    product_id = serializers.IntegerField()  # Field for product ID

    class Meta:
        model = PurchaseHistory
        fields = ['user_id', 'product_id','product_amount','price', 'total_amount']
        read_only_fields = ['created_at','price', 'total_amount']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        product_id = validated_data.pop('product_id')
        # You may want to calculate total_amount based on the provided product_id and user_id
        # Assuming total_amount is calculated elsewhere or provided in the request data
        purchase = PurchaseHistory.objects.create(user_id=user_id, product_id=product_id, **validated_data)
        return purchase

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
    class Meta:
        model = Savatcha
        fields = ['product']

    def create(self, validated_data):
        return Savatcha.objects.create(product=validated_data['product'], user=self.context['request'].user)



class SavatchaListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    class Meta:
        model = Savatcha
        fields = '__all__'

class SavatchaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savatcha
        fields = ['product']
        read_only_fields = ['created_at']





class LikedProductCreateSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = liked
        fields = ['user', 'product_id']  # Include 'user' and 'product_id'
        read_only_fields = ['user']  # Make 'user' read-only

    def create(self, validated_data):
        user = self.context['request'].user  # Get user from context
        liked_obj = liked.objects.create(user=user, **validated_data)
        return liked_obj


class LikedProductListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()
    class Meta:
        model = liked
        fields = '__all__'

