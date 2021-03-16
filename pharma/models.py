from django.db import models

# Create your models here.
class Medical_Products(models.Model):
    med_name = models.CharField(max_length=100)
    med_price = models.IntegerField()
    med_img = models.ImageField(upload_to='pictures')
    med_sale = models.BooleanField(default=False)
    med_des = models.TextField()
    med_category = models.CharField(max_length=25)
<<<<<<< HEAD
    med_type = models.CharField(max_length=25)
=======
    med_type = models.CharField(max_length=25) 
>>>>>>> b0b56b907c4346e31c9ae28e17186198ac904b79
