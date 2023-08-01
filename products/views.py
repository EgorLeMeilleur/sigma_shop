from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.apps import apps
# Create your views here.
from products.models import Product


def find_category(request):
    content_type = request.GET.get('category', 'Product')
    model = apps.get_model('products', content_type)
    return model


def sort_by_popularity_asc(request):
    products = find_category(request).objects.annotate(num_purchases=Count('purchases')).order_by('-num_purchases')
    return render(request, 'products.html', {'products': products})


def sort_by_popularity_desc(request):
    products = find_category(request).objects.annotate(num_purchases=Count('purchases')).order_by('num_purchases')
    return render(request, 'products.html', {'benefits': products})


def sort_by_price_asc(request):
    products = find_category(request).objects.order_by('price')
    return render(request, 'products.html', {'products': products})


def sort_by_price_desc(request):
    products = find_category(request).objects.all().order_by('-price')
    return render(request, 'products.html', {'products': products})


def sort_by_name_asc(request):
    products = find_category(request).objects.all().order_by('name')
    return render(request, 'products.html', {'products': products})


def sort_by_name_desc(request):
    products = find_category(request).objects.all().order_by('-name')
    return render(request, 'products.html', {'products': products})


def products_show(request):
    products = find_category(request).objects.all()
    return render(request, 'products.html', {'products': products})

