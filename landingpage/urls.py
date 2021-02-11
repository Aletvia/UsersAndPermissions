from .views import *
from django.conf import settings 
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name="main_index"),
    path('iniciar-sesion', Login.as_view(), name="login"),
    
]
