from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from products.models import Product


@login_required
def sort_by_popularity_asc(request):
    products = Product.objects.annotate(num_purchases=Count('purchases')).order_by('-num_purchases')
    return render(request, 'benefits.html', {'products': products})


@login_required
def sort_by_popularity_desc(request):
    products = Product.objects.annotate(num_purchases=Count('purchases')).order_by('num_purchases')
    return render(request, 'products.html', {'benefits': products})


@login_required
def sort_by_price_asc(request):
    products = Product.objects.all().order_by('price')
    return render(request, 'benefits.html', {'products': products})


@login_required
def sort_by_price_desc(request):
    products = Product.objects.all().order_by('-price')
    return render(request, 'products.html', {'products': products})


@login_required
def sort_by_name_asc(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'benefits.html', {'products': products})


@login_required
def sort_by_name_desc(request):
    products = Product.objects.all().order_by('-name')
    return render(request, 'products.html', {'products': products})
