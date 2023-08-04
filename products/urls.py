from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path('products/', views.products_show, name='products_show'),
    path('clothes_create/', views.clothes_create, name='clothes_create'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('sort_by_popularity_desc/', views.sort_by_popularity_desc, name='sort_by_popularity_desc'),
    path('sort_by_promotion_desc/', views.sort_by_promotion_desc, name='sort_by_promotion_desc'),
    path('sort_by_price_asc/', views.sort_by_price_asc, name='sort_by_price_asc'),
    path('sort_by_price_desc/', views.sort_by_price_desc, name='sort_by_price_desc'),
    path('sort_by_name_asc/', views.sort_by_name_asc, name='sort_by_name_asc'),
    path('sort_by_name_desc/', views.sort_by_name_desc, name='sort_by_name_desc'),
]

