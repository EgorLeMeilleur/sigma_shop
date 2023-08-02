from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path('products/', views.products_show, name='products_show'),
    path('clothes_create/', views.clothes_create, name='clothes_create'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
]
