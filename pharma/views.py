from django.shortcuts import render
from django.http import HttpResponse
from . models import Medical_Products
import json

from django.http import JsonResponse
# Create your views here.
def autocomplete(request):
    med_prods = Medical_Products.objects.all()
    
    if 'term' in request.GET:
        qs = Medical_Products.objects.filter(med_name__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.med_name)
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    return render(request,"index.html",{'med_prods' : med_prods})

def cart(request):
    return render(request,"cart.html")

def checkout(request):
    return render(request,"checkout.html")

def register(request):
    return render(request,'accounts/register.html')

def shopsingle(request,prod_id):
    prod_id = Medical_Products.objects.get(id = prod_id)
    return render(request,"shop-single.html",{'prod':prod_id})
    
def shop(request):
    med_prods = Medical_Products.objects.all()
    return render(request,"shop.html",{'med_prods' : med_prods})
def search(request):
    item = request.POST['id']
    med_prods = Medical_Products.objects.filter(med_name=item)
    print(med_prods)
    return render(request,"shop.html",{'med_prods' : med_prods})