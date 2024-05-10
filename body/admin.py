from django.contrib import admin
from body.models import *
admin.site.register([Payment,PurchaseHistory,liked,Savatcha,Category,Comments])

from .models import Product, ProductMedia

class ProductMediaInline(admin.TabularInline):
    model = Product.photos_or_videos.through  # Through model for the ManyToManyField
    # fields = ['file', 'is_home']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductMediaInline]
    # list_display = ['name']
    # fields = ['name']
    # exclude = ['photos_or_videos']

@admin.register(ProductMedia)
class ProductMediaAdmin(admin.ModelAdmin):
    pass

# class Is_homepageAdmin(admin.ModelAdmin):
#     pass

