from django.db import models

# Create your models here.
class Medical_Products(models.Model):
    med_name = models.CharField(max_length=100)
    med_price = models.IntegerField()
    med_img = models.ImageField(upload_to='pictures')
    med_sale = models.BooleanField(default=False)
    med_des = models.TextField()
    med_category = models.CharField(max_length=25)
    med_type = models.CharField(max_length=25) 

class Cart_Items(models.Model):
    item = models.ForeignKey(Medical_Products)
    quantity = models.IntegerField()

class User_Info(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_phone = models.IntegerField()
    user_address = models.CharField(max_length=100)
