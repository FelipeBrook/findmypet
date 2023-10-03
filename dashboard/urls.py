from django.contrib import admin
from django.urls import path, include
from .views import dashboard, mascota, agregar_mascota, RazaViewset, MascotasViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'apiRazas', RazaViewset, basename='raza')
router.register(r'apiMascotas', MascotasViewset, basename='mascota')

app_name = 'api'

urlpatterns = [
    path('base/', dashboard, name="base"),

    path('api/', include(router.urls)),

    path('mascota/<id>/', mascota, name="mascota"),
    path('agregarMascota/', agregar_mascota, name="agregarMascota"),
]

urlpatterns += router.urls