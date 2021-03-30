"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='pharma-home'),
    path('cart/', views.cart,name = 'pharma-cart'),
    path('checkout/', views.checkout,name = 'pharma-checkout'),
    path('shop-single/<int:prod_id>',views.shopsingle,name='pharma-shop-single'),
    path('shop/shop-single/<int:prod_id>',views.shopsingle,name='pharma-shop-single'),
    path('shop/',views.shop,name='pharma-shop'),
    path('search/',views.search,name='pharma-search'),
    path('search/shop-single/<int:prod_id>',views.shopsingle,name='pharma-shop-single'),
]
