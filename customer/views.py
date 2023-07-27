from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse

from products.models import Product
from .forms import LoginForm
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
    return render(request, 'index.html')


@login_required
def personal_cabinet(request):
    products = Product.objects.all()
    return render(request, 'personal_cabinet.html', {'products': products})
