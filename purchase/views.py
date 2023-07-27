from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from products.models import Product
from purchase.models import Purchase


def purchase(request, pk):
    user_id = request.user
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        if user_id.user_profile.balance >= product.price:
            user_id.user_profile.balance -= product.price
        else:
            return redirect('personal_cabinet')
        new_obj = Purchase(user=user_id, product=product)
        new_obj.save()
        user_id.save()
    return redirect('personal_cabinet')
