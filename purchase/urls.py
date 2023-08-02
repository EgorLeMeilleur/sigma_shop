from django.contrib import admin
from django.urls import path

from purchase import views

urlpatterns = [
    path('purchase/', views.purchase, name='purchase'),
]
