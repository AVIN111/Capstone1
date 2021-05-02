from django.urls import path, include
from . import views

urlpatterns = [
        path('accounts/', include('allauth.urls')),
        path("register", views.register, name="pharma-register"),
        path("login", views.login, name="pharma-login"),
        path("logout", views.logout, name='pharma-logout')
        ]
    
