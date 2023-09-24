from django.contrib import admin
from django.urls import path
from .views import home,contacto,login,register,exit,pet

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('pet/', pet, name='pet'),
    path('logout/', exit, name='exit'),
]
