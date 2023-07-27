from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from products.models import Product
from wishes.models import Wishes


def create_wishes(request, pk):
    user_id = request.user
    product = get_object_or_404(Product, pk=pk)
    if not Wishes.objects.filter(user=user_id, product=product).exists():
        new_obj = Wishes(user=user_id, product=product)
        new_obj.save()
    return redirect('personal_cabinet')


def delete_wishes(request, pk):
    user_id = request.user
    product = get_object_or_404(Product, pk=pk)
    Wishes.objects.filter(user=user_id, product=product).delete()
    return redirect('personal_cabinet')
