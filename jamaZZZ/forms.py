from django.forms import ModelForm
from .models import Items
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ItemsForm(ModelForm):
     class Meta:
        model = Items
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


