
from django.urls import path
from body.views import *
from custom_admin.views import *


urlpatterns = [
    path('product-menu-for-owner/', ProductListforOwnerAPIView.as_view(), name='product-owner-menu'),
    path('product-create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('product-update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('product-delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('product-owner-info/<int:pk>/',ProductownerinfoListAPIView.as_view(), name='product-owner-info'),

    path('category-list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category-products-list/<int:pk>/', CategoryProductsListAPIView.as_view(), name='category-products-list'),
    path('category-create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category-update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('category-delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name='category-delete'),
    ]