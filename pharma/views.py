from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Payment,Medical_Products,Product_Reviews,Shop_Cart
import json

from django.http import JsonResponse

from .forms import PaymentForm
import razorpay
from .models import Payment


def medicine_payment(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return render(request,"cart.html")
        else:
            cart1 = Shop_Cart.objects.all().filter(user = request.user)
            total = 0
            details = []
            quantity = []
            for item in cart1:
                total += item.product.med_price * item.quantity
                details.append(item.product.med_name)
                quantity.append(item.quantity)
        amount = total * 100

        # create Razorpay client
        client = razorpay.Client(auth=('rzp_test_Ok48NDbUNUMZIL', 'LcaDh1yiIoY0VOWOKj5EzZ3r'))

        # create order
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            order = Payment(
                user=request.user,
                amount=amount,
                order_id=order_id,
                quantity=quantity,
                names=details
            )
            order.save()

            form = PaymentForm(request.POST or None)
            return render(request, 'payment.html', {'form': form, 'payment': response_payment})

    form = PaymentForm()
    
    return render(request, 'payment.html', {'form': form})


def payment_status(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    # client instance
    client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'LcaDh1yiIoY0VOWOKj5EzZ3r'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        order = Payment.objects.get(order_id=response['razorpay_order_id'])
        order.razorpay_payment_id = response['razorpay_payment_id']
        order.paid = True
        order.save()
        return render(request, 'payment_status.html', {'status': True})
    except:
        return render(request, 'payment_status.html', {'status': False})

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
    if not request.user.is_authenticated:
        return render(request,"cart.html")
    else:
        cart1 = Shop_Cart.objects.all().filter(user = request.user)
        total = 0
        for item in cart1:
            total += item.product.med_price * item.quantity
            print(total)
        return render(request,"cart.html",{'cart':cart1,'total':total})

def checkout(request):

    if not request.user.is_authenticated:
        return render(request,"cart.html")
    else:
        cart1 = Shop_Cart.objects.all().filter(user = request.user)
        total = 0
        for item in cart1:
            total += item.product.med_price * item.quantity
            print(total)
        return render(request,"checkout.html",{'cart':cart1,'total':total})

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
def shopsingleform(request,prod_id):
    # product = get_object_or_404(Medical_Products, slug=prod_id)
    # prod_id = Medical_Products.objects.get(id = prod_id)
    prod_id = Medical_Products.objects.get(id = prod_id)
    review = Product_Reviews.objects.all()
    if request.method == 'POST' and request.user.is_authenticated:
        
        quantity = int(request.POST['quantity'])
        cart1 = Shop_Cart.objects.create(quantity = quantity,user=request.user,product=prod_id)
        return render(request,"shop-single.html",{'prod':prod_id})
    else:
        return render(request,"register.html")

def shop(request):
    med_prods = Medical_Products.objects.all()
    return render(request,"shop.html",{'med_prods' : med_prods})
def search(request):
    item = request.POST['id']
    med_prods = Medical_Products.objects.filter(med_name=item)
    print(med_prods)
    return render(request,"shop.html",{'med_prods' : med_prods})