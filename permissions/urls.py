from .views import Permissions
from . import views
from django.conf import settings 
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', Permissions.as_view(), name="permission_list"),
]
