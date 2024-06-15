from django.urls import path
from body.views import *
from custom_admin.views import *

urlpatterns = [
    # Product URLs
    path('product-menu/', ProductMenuAPIView.as_view(), name='product-menu'),
    path('product-owner-info/<int:pk>/',ProductownerinfoListAPIView.as_view(), name='product-owner-info'),
    path('product-by-id/<int:pk>/', ProductByIDAPIView.as_view(), name='product-detail'),


    # Purchase history URL
    path('purchase-amount-history/', PurchaseHistoryAPIView.as_view(), name='purchase-amount-history'),
    path('purchase-amount-create/',PurchaseHistoryCreateAPIView.as_view(), name='purchase-create'),

    # Savatcha URLs
    path('savatcha-create/', SavatchaCreateAPIView.as_view(), name='savatcha-create'),
    path('savatcha-list/', SavatchaListAPIView.as_view(), name='savatcha-list'),
    path('savatcha-update/<uuid:uuid>/', SavatchaUpdateAPIView.as_view(), name='savatcha-update'),
    path('savatcha-delete/<uuid:uuid>/', SavatchaDeleteAPIView.as_view(), name='savatcha-delete'),

    # Category URLs
    path('category-list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category-products-list/<int:pk>/', CategoryProductsListAPIView.as_view(), name='category-products-list'),


    # Liked Products URL
    path('liked-products/', LikedProductListAPIView.as_view(), name='liked-product-list'),
    path('liked-product-delete/<uuid:uuid>/', LikedProductDeleteAPIView.as_view(), name='liked-product-delete'),

    path('products-liked-users/<int:product_id>/', LikedUserListAPIView.as_view(), name='liked-users-list'),

    path('liked-products-create/', LikedProductCreateAPIView.as_view(), name='liked-product-create'),
    path('get-app-version/',GetAppVersionListAPIView.as_view(), name='get-app-version')
    ]