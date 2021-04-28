from django.contrib import admin

from .models import Medical_Products,Product_Reviews
# Register your models here.
admin.site.register(Medical_Products)
admin.site.register(Product_Reviews)