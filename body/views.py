import uuid

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (
    ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from body.models import Product, Category
from body.permissions import IsOwner
from body.serialize import *
from custom_admin.serialize import CategoryListSerializer


class ProductMenuAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    # pagination_class = FlexiblePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category']  # Specify the fields you want to filter on
    ordering_fields = ['price']
    search_fields = ['name']

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     category = self.request.query_params.get('category')
    #     if category:
    #         queryset = queryset.filter(category=category)
    #     return queryset

class ProductByIDAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get_object(self):
        try:
            obj = self.get_queryset().get(pk=self.kwargs.get('pk'))
            self.check_object_permissions(self.request, obj)
            return obj
        except Product.DoesNotExist:
            raise NotFound("Product not found.")

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['name']
    ordering_fields = ['name']
    search_fields = ['name']

    def get_object(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

class CategoryProductsListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category']  # Use filterset_fields for exact filtering

    def get_queryset(self):
        category_id = self.kwargs.get('pk') # Access pk from URL parameters
        return self.queryset.filter(category_id=category_id)


class PurchaseHistoryCreateAPIView(CreateAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistoryCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        product_id = self.request.data.get('product_id')
        # Retrieve the product and calculate price and product_amount
        product = Product.objects.get(pk=product_id)
        price = product.price # Assuming product_amount is 1 for simplicity, adjust as needed
        serializer.save(price=price)

class PurchaseHistoryAPIView(ListAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['price']
    search_fields = ['product__name']

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class SavatchaCreateAPIView(CreateAPIView):
    queryset = Savatcha.objects.all()
    serializer_class = SavatchaCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        product_amount = request.data.get('product_amount')
        if product_id is None:
            return Response({"product": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data={'product': product_id, 'product_amount':product_amount})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer.save(uuid=uuid.uuid4())
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SavatchaUpdateAPIView(UpdateAPIView):
    queryset = Savatcha.objects.all()
    serializer_class = SavatchaUpdateSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, uuid=self.kwargs.get('uuid'))
        self.check_object_permissions(self.request, obj)
        return obj




class SavatchaListAPIView(ListAPIView):
    serializer_class = SavatchaListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['name']      # Add the fields you want to search

    def get_queryset(self):
        user = self.request.user
        queryset = Savatcha.objects.filter(user=user)
        return queryset


class SavatchaDeleteAPIView(DestroyAPIView):
    queryset = Savatcha.objects.all()
    serializer_class = SavatchaListSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        uuid = self.kwargs.get('uuid')
        obj = get_object_or_404(queryset, uuid=uuid)
        self.check_object_permissions(self.request, obj)
        return obj


class LikedProductListAPIView(ListAPIView):
    serializer_class = LikedProductListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        user = self.request.user
        queryset = liked.objects.filter(user=user)
        return queryset

class LikedProductDeleteAPIView(DestroyAPIView):
    queryset = liked.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsOwner]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        uuid = self.kwargs.get('uuid')
        obj = get_object_or_404(queryset, uuid=uuid)
        self.check_object_permissions(self.request, obj)
        return obj
class LikedUserListAPIView(ListAPIView):
    serializer_class = LikedUserSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']  # Assuming you're passing product_id in URL
        return User.objects.filter(id__in=liked.objects.filter(product_id=product_id).values_list('user_id', flat=True))



class LikedProductCreateAPIView(CreateAPIView):
    serializer_class = LikedProductCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        product_id = serializer.validated_data['product_id']

        if liked.objects.filter(user=user, product_id=product_id).exists():
            raise serializers.ValidationError("User has already liked this product")

        serializer.save(uuid=uuid.uuid4())
        print(str(serializer.data))
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetAppVersionListAPIView(ListAPIView):
    queryset = Versions.objects.all()
    serializer_class = GetAppVersionSerializer

