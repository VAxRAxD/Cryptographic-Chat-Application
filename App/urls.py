from django.urls import path
from . import views

urlpatterns = [
    path('lobby/<str:room_name>/', views.lobby, name="lobby"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('home/', views.home ,name="home"),
]