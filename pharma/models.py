from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Medical_Products(models.Model):
    med_name = models.CharField(max_length=100)
    med_price = models.IntegerField()
    med_img = models.ImageField(upload_to='pictures')
    med_sale = models.BooleanField(default=False)
    med_des = models.TextField()
    med_category = models.CharField(max_length=25)
    med_type = models.CharField(max_length=25) 

class Product_Reviews(models.Model):
    product = models.ForeignKey(Medical_Products, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    one_word_review = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)
class Payment(models.Model):
    amount = models.CharField(max_length=100)
    names = ArrayField(models.CharField(max_length=550,blank=True),default=list)
    quantity = ArrayField(models.IntegerField(blank=True),default=list)
    user = models.ForeignKey(User, related_name='payment', on_delete=models.SET_NULL,null=True)
    order_id = models.CharField(max_length=100,blank=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True)
    paid = models.BooleanField(default=False)
class Shop_Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Medical_Products, related_name='cart', on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()

    """ def __str__(self):
        return self.product.title
    
    def price(self):
        return (self.product.med_price)
    
    def amount(self):
        return (self.quantity * self.product.med_price)
        
class Shop_Cartform(ModelForm):
    class meta:
        model  = Shop_Cart
        fields  = ['quantity']"""
    