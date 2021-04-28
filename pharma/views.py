from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Medical_Products,Product_Reviews
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
# def reviews(request):

def register(request):
    return render(request,'accounts/register.html')

def shopsingle(request,prod_id):
    # product = get_object_or_404(Medical_Products, slug=prod_id)
    # prod_id = Medical_Products.objects.get(id = prod_id)
    prod_id = Medical_Products.objects.get(id = prod_id)
    review = Product_Reviews.objects.all()
    if request.method == 'POST' and request.user.is_authenticated:
        one_word = request.POST['choice']
        content = request.POST['content']
        rating = int(request.POST['rating'])
        review1 = Product_Reviews.objects.create(one_word_review = one_word,content=content,rating= rating,product = prod_id,user = request.user)
        
    review = Product_Reviews.objects.all()
    return render(request,"shop-single.html",{'prod':prod_id,'reviews':review})
    
def shop(request):
    med_prods = Medical_Products.objects.all()
    return render(request,"shop.html",{'med_prods' : med_prods})
def search(request):
    item = request.POST['id']
    med_prods = Medical_Products.objects.filter(med_name=item)
    print(med_prods)
    return render(request,"shop.html",{'med_prods' : med_prods})