from django.db import models
from django.contrib.auth.models import User
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