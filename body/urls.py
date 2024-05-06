from django.urls import path
from body.views import *

urlpatterns = [
    # Product URLs
    path('product-menu/', ProductMenuAPIView.as_view(), name='product-menu'),
    # path('product-menu-for-owner/', ProductListforOwnerAPIView.as_view(), name='product-owner-menu'),
    # path('product-create/', ProductCreateAPIView.as_view(), name='product-create'),
    # path('product-update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    # path('product-delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete'),

    # Purchase history URL
    path('purchase-amount-history/', PurchaseHistoryAPIView.as_view(), name='purchase-amount-history'),
    path('purchase-amount-create/',PurchaseHistoryCreateAPIView.as_view(), name='purchase-create'),

    # Savatcha URLs
    path('savatcha-create/', SavatchaCreateAPIView.as_view(), name='savatcha-create'),
    path('savatcha-list/', SavatchaListAPIView.as_view(), name='savatcha-list'),
    # path('savatcha-update/<int:pk>/', SavatchaUpdateAPIView.as_view(), name='savatcha-update'),
    path('savatcha-delete/<int:pk>/', SavatchaDeleteAPIView.as_view(), name='savatcha-delete'),

    # Category URLs
    path('category-list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category-products-list/<int:pk>/', CategoryProductsListAPIView.as_view(), name='category-products-list'),
    # path('category-create/', CategoryCreateAPIView.as_view(), name='category-create'),
    # path('category-update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category-update'),
    # path('category-delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name='category-delete'),

    # Liked Products URL
    path('liked-product-create/', LikedProductCreateAPIView.as_view(), name='liked-product-create'),
    path('liked-product-list/', LikedProductListAPIView.as_view(), name='liked-product-list'),
    path('api/liked-product-delete/<int:pk>/', LikedProductDeleteAPIView.as_view(), name='liked-product-delete'),
]
