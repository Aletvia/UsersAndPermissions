from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import UserForm, ChangeUserForm
from django.views.generic import ListView, CreateView

"""
Class View que despliega la lista de ususarios sin permisos de tipo staff y 
devuelve el resultado de la búsqueda.
"""
class Users(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    template_name = 'auth/user_list.html'
    model = User
    context_object_name = 'users'

    def get_queryset(self):
        user_name =  self.request.GET.get('search_user', None)
        if user_name:
            return User.objects.filter(is_staff=False, first_name=user_name)
        else:
            return User.objects.filter(is_staff=False)


class CreateUser(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self,request):

        return render( request, 'auth/user_form.html', {
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

        return render( request, 'auth/user_form.html', {
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
            return render( request, 'auth/user_form.html', {
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