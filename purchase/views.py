from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from products.models import Product
from purchase.models import Purchase
from sigma_shop.settings import EMAIL_HOST_USER
from wishes.models import Wishes
from django.core.mail import send_mail
from django.core.mail import EmailMessage


def purchase(request):
    if request.method == 'POST':
        user_id = request.user
        wishes = Wishes.objects.filter(user=user_id)
        if wishes:
            subject = 'Заказ от ' + user_id.username + '. Телефон: ' + str(user_id.user_profile.phone_number) + '. Электронная почта: ' + str(user_id.user_profile.email) + '. '
            message = ''
            for wish in wishes:
                new_obj = Purchase(user=user_id, product=wish.product, quantity=wish.quantity)
                message += 'Продукт ' + wish.product.name + ' в количестве ' + str(wish.quantity) + ' шт. Цена: ' + str(wish.product.get_discounted_price()) + ' р.\n'
                new_obj.save()
                wish.delete()
            email = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                ['sigmamaleshop@yandex.ru'])
            email.send()
    return redirect('personal_cabinet')
