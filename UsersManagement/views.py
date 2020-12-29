from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from UsersManagement.forms import UserForm

class Users(View):
    def get(self, request):
        return render(request, 'users/index.html', {
            'title' : 'Usuarios'
        })

class CreateUser(View):
    def get(self,request):
        register_form = UserForm()

        return render( request, 'users/user_form.html', {
            'title' : 'Registrar usuario',
            'register_form' : register_form
        })
    def post(self, request):
        print('POST entra')
        register_form = UserForm( request.POST )

        if register_form.is_valid():
            print('Correcto')
            register_form.save()
            messages.success(request, 'El registro se ha realizado con éxito')
            return redirect( 'users_list' )
        else:
            return redirect('create_users')

