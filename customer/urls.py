from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.login_user, name='login_user'),
    path('', views.beginning_page, name='beginning_page'),
    path('personal_cabinet/', views.personal_cabinet, name='personal_cabinet'),
    path('registration/', views.register, name='register')
]
