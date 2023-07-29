from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Customer


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'login'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'password'}))


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class RegisterProfileForm(forms.Form):
    surname = forms.CharField(max_length=255, required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    city = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Customer
        fields = ('surname', 'first_name', 'last_name', 'email', 'balance', 'city')

