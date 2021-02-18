from django import forms
from django.core import validators

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""
Formulario para crear un usuario
"""
class UserForm( UserCreationForm ):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


"""
Formulario para editar información un usuario
"""
class ChangeUserForm( forms.ModelForm ):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']