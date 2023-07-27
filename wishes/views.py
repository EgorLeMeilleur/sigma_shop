from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from products.models import Product
from wishes.models import Wishes


def purchase(request, pk):
    user_id = request.user
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        new_obj = Wishes(user=user_id, product=product)
        new_obj.save()
    return redirect('personal_cabinet')
