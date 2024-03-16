from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('company/<int:company_id>/', views.company_products, name='company_products'),
    path('checkout/', views.checkout, name='checkout'),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('myaccount', views.myaccount, name='myaccount'),
    path('checkout/', views.checkout, name='checkout'),
    path('myorder', views.myorder, name='myorder'),
    
      # Ensure the name is 'company_products'
    # Example pattern
    # Add more URL patterns here as needed
]
