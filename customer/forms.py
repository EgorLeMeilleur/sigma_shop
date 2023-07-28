from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Customer


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'login'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'password'}))


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileForm(forms.Form):
    surname = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'surname'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'first_name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'last_name'}))
    city = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'city'}))
    balance = forms.DecimalField(label="", widget=forms.TextInput(attrs={'id': 'balance'}))
    email = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'id': 'email'}))

    class Meta:
        model = Customer
        fields = ('surname', 'first_name', 'last_name', 'email', 'balance', 'city')
