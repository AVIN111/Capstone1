from django.shortcuts import render
from django.http import HttpResponse
from . models import Medicine
# Create your views here.
def index(request):
    med1=Medicine()
    med1.name='Crocin'
    med1.price=100
    return render(request,"index.html",{'med1':med1})

def cart(request):
    return render(request,"cart.html")

def checkout(request):
    return render(request,"checkout.html")

def register(request):
    return render(request,'accounts/register.html')
