from django.contrib import admin

from .models import Medical_Products,Product_Reviews,Shop_Cart,Payment
# Register your models here.
admin.site.register(Medical_Products)
admin.site.register(Product_Reviews)
admin.site.register(Shop_Cart)
admin.site.register(Payment)