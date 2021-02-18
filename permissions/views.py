from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import UserForm, ChangeUserForm

class Permissions(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        groups = Group.objects.all()
        print(groups)
        users = User.objects.filter(is_staff=False)
        return render(request, 'permissions/index.html', {
            'title' : 'Permisos',
            'groups' : groups
        })
