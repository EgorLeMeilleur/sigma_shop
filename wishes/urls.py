from django.contrib import admin
from django.urls import path

from wishes import views

urlpatterns = [
    path('create_wishes/<int:pk>/', views.create_wishes, name='create_wishes'),
    path('delete_wishes/<int:pk>/', views.delete_wishes, name='delete_wishes'),
]
