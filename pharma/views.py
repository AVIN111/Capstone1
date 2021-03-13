from django.shortcuts import render
from django.http import HttpResponse
from . models import Medical_Products
# Create your views here.
def index(request):
    med_prods = Medical_Products.objects.all()



    return render(request,"index.html",{'med_prods' : med_prods})

def cart(request):
    return render(request,"cart.html")

def shopsingle(request,prod_id):
    prod_id = Medical_Products.objects.get(id = prod_id)
    return render(request,"shop-single.html",{'prod':prod_id})
def shop(request):
    med_prods = Medical_Products.objects.all()
    return render(request,"shop.html",{'med_prods' : med_prods})