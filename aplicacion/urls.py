from django.contrib import admin
from django.urls import path
from .views import home,contacto,login,pet

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('login/', login, name='login'),
    path('pet/', pet, name='pet')
]
