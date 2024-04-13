from django.contrib import admin
from body.models import *
admin.site.register([User,Payment,Product,PurchaseHistory,liked,Savatcha,Category])