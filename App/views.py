from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from json import dumps
from . authenticator import *

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("lobby",room_name="test")
    return render(request,'App/login.html')

@unauthenticated_user
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect("lobby",room_name="test")
    return render(request,'App/register.html')

@authenticated_user
def lobby(request,room_name):
    user=request.user
    return render(request,'App/lobby.html',{"room_name":room_name,"user":user})

@authenticated_user
def home(request):
    users=dumps([str(name) for entry in list(User.objects.values_list('username')) for name in entry])
    return render(request,'App/home.html',{"users":users,'user':request.user})
