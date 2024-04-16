from django.urls import path
from body.views import *

urlpatterns = [
    #product abs
    path('product-menu/', ProductMenuAPIView.as_view(), name='product-menu'),
    path('product-menu-for-owner/<int:pk>/', ProductListforounerAPIView.as_view(), name='product-owner-menu'),
    path('product-update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('product-delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete'),

    # Purchase_count
    path('purchase-amount-history', PurchaseHistoryAPIView.as_view(), name='purchase-amount-history'),

    #Savatcha
    path('savatcha-create/', SavatchaCreateAPIView.as_view(), name='savatcha-create'),
    path('savatcha-update/', SavatchaUpdateAPIView.as_view(), name='savatcha-update'),
    path('savatcha-delete/', SavatchaDeleteAPIView.as_view(), name='savatcha-delete'),

    #category
    path('category-list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category-create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category-update/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('category-delete/', CategoryDeleteAPIView.as_view(), name='category-delete'),

    #liked Products
    path('liked-product-create', LikedProductCreateAPIView.as_view(), name='liked-product-create'),
]
