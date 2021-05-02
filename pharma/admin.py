from django.contrib import admin

from .models import Medical_Products,Product_Reviews,Shop_Cart
# Register your models here.
admin.site.register(Medical_Products)
admin.site.register(Product_Reviews)
admin.site.register(Shop_Cart)