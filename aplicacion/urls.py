from django.contrib import admin
from django.urls import path,include
from .views import agregar_producto, home,contacto,login,exit,pet,signup_view,eliminar_producto,restar_producto,limpiar_carrito,carrito
from . import views



urlpatterns =[
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('login/', login, name='login'),
    # path('register/', register, name='register'),
    path('pet/', pet, name='pet'),
    path('logout/', exit, name='exit'),
    path('accounts/', include('allauth.urls')),
    path('accounts/signup/', signup_view, name='signup'),
    path('adoptame/', views.adoptame, name='adoptame'),
    path('lugares/', views.lugares, name='lugares'),
    path('ecommerce/', views.ecommerce, name='ecommerce'),
    path('mascotas/<int:mascota_id>/', views.perfil_mascota, name='perfil_mascota'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    path('carrito/', carrito, name='carrito'),
    

   
]
