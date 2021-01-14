from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from UsersManagement.forms import UserForm, ChangeUserForm

class Users(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        users = User.objects.filter(is_staff=False)
        return render(request, 'users/index.html', {
            'title' : 'Usuarios',
            'users' : users
        })


class CreateUser(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self,request):

        return render( request, 'users/user_form.html', {
            'title' : 'Registrar usuario'
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


class UpdateUser(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request, id):
        user_u = User.objects.get(id=id)

        return render( request, 'users/user_form.html', {
            'title' : 'Editar usuario',
            'user_u' : user_u
        })

    def post(self, request, id):
        user_u = User.objects.get(id=id)
        form = ChangeUserForm(request.POST,instance=user_u)
        print('///////////////////////////////////Actualizando usuario///////////////////////////////////')
        if form.is_valid():
            form.cleaned_data
            form.save()
            messages.success(request, 'El usuario se ha actualizado con éxito')
            return redirect('users_list')
        else:
            print(form.errors)
            form = UserForm()
            messages.error(request, 'UPS ... existe un problema con alguno de los campos. Por favor verifica y vuelve a intentarlo.')
            return render( request, 'users/user_form.html', {
                'title' : 'Editar usuario',
                'user_u' : user_u
            })


class DeleteUser(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def post(self, request, id):
        usr = User.objects.get(id=id)
        usr.delete()
        messages.success(request, 'El usuario se ha eliminado con éxito')
        return redirect('users_list')


def LogoutUser(request):
    logout(request)
    return redirect('login')