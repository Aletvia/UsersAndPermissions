from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout

class Index(View):
    def get(self, request):
        return render(request, 'landingpage/index.html')


class Login(View):
    def get(self, request):
        return render(request, 'landingpage/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('users_list')
        else:
            messages.warning(request, 'No te has identificado correctamente')
            return redirect('login')
