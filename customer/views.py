from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse

from products.models import Product, Clothes
from purchase.models import Purchase
from wishes.models import Wishes
from .forms import LoginForm, RegisterUserForm, RegisterProfileForm
from .models import Customer


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('personal_cabinet')
            else:
                form.add_error(None, 'Incorrect username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def beginning_page(request):
    return render(request, 'beginning_page.html')


def register_user(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        profile_form = RegisterProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.user_profile.surname = profile_form.cleaned_data['surname']
            user.user_profile.first_name = profile_form.cleaned_data['first_name']
            user.user_profile.last_name = profile_form.cleaned_data['last_name']
            user.user_profile.email = profile_form.cleaned_data['email']
            user.user_profile.city = profile_form.cleaned_data['city']
            user.user_profile.is_admin = False
            user.save()
            return redirect('login_user')
    else:
        user_form = RegisterUserForm()
        profile_form = RegisterProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def personal_cabinet(request):
    user = request.user
    if user.user_profile.is_admin:
        purchases = Purchase.objects.all()
        return render(request, 'administration_cabinet.html', {'purchases': purchases})
    else:
        products = Product.objects.all()
        purchases = Purchase.objects.filter(user=user)
        wishes = Wishes.objects.filter(user=user)
        return render(request, 'personal_cabinet.html', dict(products=products, purchases=purchases, wishes=wishes))


@login_required
def logout(request):
    return redirect('beginning_page')


