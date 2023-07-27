from django.contrib import admin
from django.urls import path

from wishes import views

urlpatterns = [
    path('wish/<int:pk>/', views.wish, name='wish'),
]