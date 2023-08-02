from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from products.models import Product
from purchase.models import Purchase
from wishes.models import Wishes


def purchase(request):
    if request.method == 'POST':
        user_id = request.user
        wishes = Wishes.objects.filter(user=user_id)
        if wishes:
            for wish in wishes:
                new_obj = Purchase(user=user_id, product=wish.product, quantity=wish.quantity)
                new_obj.save()
                wish.delete()
    return redirect('personal_cabinet')
