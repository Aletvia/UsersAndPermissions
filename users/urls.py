from .views import *
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', Users.as_view(), name="users_list"),
    path('registrar-usuario', CreateUser.as_view(), name="create_users"),
    path('editar-usuario/<str:id>', UpdateUser.as_view(), name="update_user"),
    path('eliminar-usuario/<str:id>', DeleteUser.as_view(), name="delete_user"),
    path('logout', LogoutUser, name="logout")
]
