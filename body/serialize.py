from django.contrib.auth import get_user_model
from rest_framework import serializers

from custom_admin.serialize import ProductListSerializer
from .models import PurchaseHistory, Savatcha, liked, Payment, Versions

User = get_user_model()

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'




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



class SavatchaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savatcha
        fields = ['product','product_amount','uuid']

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
        fields = ['product','product_amount']
        read_only_fields = ['created_at']



class PurchaseHistorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    product = ProductListSerializer()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    # Define a serializer method field to fetch product_amount
    product_amount = serializers.SerializerMethodField()

    class Meta:
        model = PurchaseHistory
        fields = ['product_amount', 'price', 'user', 'product', 'total_amount']
        read_only_fields = ['created_at']

    def get_product_amount(self, obj):
        # Assuming PurchaseHistory has a ForeignKey to Savatcha and related_name is 'purchase_history'
        savatcha_instance = obj.product.purchase_history.first()
        if savatcha_instance:
            serializer = SavatchaListSerializer(savatcha_instance)
            return serializer.data['product_amount']
        return None


class LikedProductCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    product_id = serializers.IntegerField()

    class Meta:
        model = liked
        fields = ['user', 'product_id','uuid']  # Include 'user' and 'product'
        read_only_fields = ['user','uuid']  # Make 'user' read-only


class LikedProductListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = liked
        fields = '__all__'



# class ProductLikedListSerializer(serializers.ModelSerializer):
#     liked = LikedProductListSerializer(many=True, read_only=True)
#     user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Product
#         fields = ['id', 'liked', 'user']



class LikedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class LikedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = liked
        fields = ['user', 'product', 'liked_status']


class GetAppVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Versions
        fields = '__all__'
        read_only_fields = ['created_at']