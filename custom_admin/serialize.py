from django.contrib.auth import get_user_model
from rest_framework import serializers

from body.models import Product, Category, ProductMedia

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



#ex_owner field will delete couse of new incoming features like abilty to create a product permission for all user who want to be costumer!
class ProductListSerializer(serializers.ModelSerializer):
    photos_or_videos = ProductMediaSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','product_owner', 'photos_or_videos','category' ,'price', 'product_comment','ex_owner_number','ex_owner_tg_username']
        read_only_fields = ['created_at']
class ProductListforSavatchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']
        read_only_fields = ['created_at']

class ProductownerinfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
