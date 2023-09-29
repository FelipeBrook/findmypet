from django.contrib import admin
from django.urls import path,include
from .views import home,contacto,login,exit,pet,signup_view

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('login/', login, name='login'),
    # path('register/', register, name='register'),
    path('pet/', pet, name='pet'),
    path('logout/', exit, name='exit'),
    path('accounts/', include('allauth.urls')),
    path('accounts/signup/', signup_view, name='signup'),

   
]
