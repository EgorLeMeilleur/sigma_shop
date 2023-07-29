from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from products.models import Product
from purchase.models import Purchase
from wishes.models import Wishes


def purchase(request, pk):
    if request.method == 'POST':
        user_id = request.user
        product = get_object_or_404(Product, pk=pk)
        if Wishes.objects.filter(user=user_id, product=product):
            wish = get_object_or_404(Wishes, user=user_id, product=product)
            new_obj = Purchase(user=user_id, product=product,
                               quantity=wish.quantity)
            new_obj.save()
            wish.delete()
    return redirect('personal_cabinet')
