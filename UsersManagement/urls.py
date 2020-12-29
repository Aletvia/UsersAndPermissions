from .views import *
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', Users.as_view(), name="users_list"),
    path('registrar-usuario', CreateUser.as_view(), name="create_users"),
]
