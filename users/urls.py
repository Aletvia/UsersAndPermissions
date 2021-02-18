from .views import *
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', Users.as_view(), name="users_list"),
    path('registrar-usuario', CreateUser.as_view(), name="create_users"),
    path('<pk>/editar', UpdateUser.as_view(), name="update_user"),
    path('<pk>/eliminar', DeleteUser.as_view(), name="delete_user"),
    path('logout', LogoutUser, name="logout")
]
