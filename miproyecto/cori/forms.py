from django import  forms
from django.forms import ModelForm
from .models import negocio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class negocioForm(ModelForm):
    class Meta:
        model = negocio
        fields = ['nombre', 'ubicacion', 'tipo_negocio', 'descripcion', 'image']

class CustomUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password1', 'password2' ]