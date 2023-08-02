from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.apps import apps
from PIL import Image
from products.forms import ClothesCreate
from products.models import Product, TShirt, Clothes, Sweatshirt, Hoody, ProductImage


def create_object_type(model_name):
    if model_name == 'TShirt':
        obj = TShirt()
        obj.save()
        return obj
    elif model_name == 'Sweatshirt':
        obj = Sweatshirt()
        obj.save()
        return obj
    elif model_name == 'Hoody':
        obj = Hoody()
        obj.save()
        return obj
    else:
        raise ValueError('Invalid model name')


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
    products = find_category(request).objects.prefetch_related('productimage_set').all()
    return render(request, 'products.html', {'products': products})


@login_required
def clothes_create(request):
    if request.method == 'POST':
        form = ClothesCreate(request.POST, request.FILES)
        if form.is_valid():
            type_clothes = form.cleaned_data['type']
            clothes = create_object_type(type_clothes)
            clothes.size = form.cleaned_data['size']
            clothes.color = form.cleaned_data['color']
            clothes.price = form.cleaned_data['price']
            clothes.name = form.cleaned_data['name']
            clothes.material = form.cleaned_data['material']
            clothes.description = form.cleaned_data['description']
            images = request.FILES.getlist('images')
            for image in images:
                img = Image.open(image)
                if not img.format.lower() in ['jpeg', 'png', 'jpg']:
                    raise ValidationError('Unsupported file format.')
                product_image = ProductImage()
                product_image.image = image
                product_image.product = clothes
                product_image.save()
            clothes.save()
            return redirect('products_show')
    else:
        form = ClothesCreate()
    return render(request, 'clothes_create.html', {'form': form})


@login_required
def delete_product(request, pk):
    get_object_or_404(Product, pk=pk).delete()
    return redirect('products_show')

