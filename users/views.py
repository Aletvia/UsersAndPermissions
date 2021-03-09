from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.forms import UserForm, ChangeUserForm

"""
(ListView) Clase que despliega la lista de ususarios sin permisos de tipo staff y 
devuelve el resultado de la búsqueda.
"""
class Users(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    template_name = 'auth/user_list.html'
    model = User
    context_object_name = 'users'
    paginate_by = 5

    def get_queryset(self):
        user_name =  self.request.GET.get('search_user', None)
        if user_name:
            return User.objects.filter(is_staff=False, first_name=user_name)
        else:
            return User.objects.filter(is_staff=False)


"""
(CreateView) Clase para crear un nuevo ususario.
"""
class CreateUser(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = User
    form_class = UserForm
    template_name = 'auth/user_form.html'
    success_url ="/usuarios"
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registrar usuario"
        return context


"""
(UpdateView) Clase que permite actualizar la información
del ususario.
"""
class UpdateUser(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = User
    form_class = ChangeUserForm
    template_name = 'auth/user_form.html'
    success_url ="/usuarios"
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar usuario"
        return context


"""
(DeleteView) Clase que elimina el usuario seleccionado.
"""
class DeleteUser(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = User
    success_url ="/usuarios"


"""
Función que cierra la sesión del usuario autenticado.
"""
def LogoutUser(request):
    logout(request)
    return redirect('login')