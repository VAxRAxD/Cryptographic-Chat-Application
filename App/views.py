from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . authenticator import *

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("lobby")
    return render(request,'App/login.html')

@unauthenticated_user
def registerPage(request):
    return render(request,'App/register.html')

@authenticated_user
def lobby(request,room_name):
    return render(request,'App/lobby.html',{"room_name":room_name})
