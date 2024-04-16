from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from body.permissions import IsOwner
from body.serialize import *

class ProductMenuAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category']  # Specify the fields you want to filter on

    # Optionally, you can specify ordering and search fields as well
    ordering_fields = ['price']
    search_fields = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        # You can customize filtering logic here based on query parameters
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

class ProductListforounerAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category']
    ordering_fields = ['price']
    search_fields = ['name']

    def get_owner(self):
        qs = super(ProductListforounerAPIView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset
class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category']
    ordering_fields = ['price']
    search_fields = ['name']

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListforounerAPIView
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category']
    ordering_fields = ['price']
    search_fields = ['name']

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class PurchaseHistoryAPIView(ListAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = []
    ordering_fields = ['price']
    search_fields = ['name']
    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class SavatchaCreateAPIView(CreateAPIView):
    queryset = Savatcha.objects.all()
    serializer_class = SavatchaCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class SavatchaUpdateAPIView(UpdateAPIView):
    queryset = Savatcha.objects.all()
    serializer_class = SavatchaCreateSerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)

class SavatchaDeleteAPIView(DestroyAPIView):

    queryset = Savatcha.objects.all()
    serializer_class = SavatchaListSerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['name']
    ordering_fields = ['name']
    search_fields = ['name']
    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset
class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)

class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)

class LikedProductCreateAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = LikedProductCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)



