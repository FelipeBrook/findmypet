from django.shortcuts import render, redirect, get_object_or_404
from aplicacion.models import MascotaUser, UserProfile, TipoMascota, RazaMascota
from rest_framework import viewsets
from django.urls import reverse
from .serializers import RazaSerializer, MascotasSerializer

class RazaViewset(viewsets.ModelViewSet):
    queryset = RazaMascota.objects.all()
    serializer_class = RazaSerializer

    def get_queryset(self):
        razas = RazaMascota.objects.all()

        tipo = self.request.GET.get('tipo')

        if tipo:
            razas = razas.filter(tipo_mascota=tipo)
        return razas

class MascotasViewset(viewsets.ModelViewSet):
    queryset = MascotaUser.objects.all()
    serializer_class = MascotasSerializer

    def perform_create(self, serializer):
        serializer.save(dueño=self.request.user)
# Create your views here.
def dashboard(request):
    mascotas = MascotaUser.objects.filter(dueño=request.user)
    usuario = UserProfile.objects.filter(user=request.user)
    context = {
        'mascotas': mascotas,
        'usuario': usuario
    }
    return render(request, 'dashboard/base.html', context)

def agregar_mascota(request):
    usuario = UserProfile.objects.filter(user=request.user)
    tipo = TipoMascota.objects.all()
    nombre_url_creacion_mascota = reverse('api:mascota-list')
    nombre_url_razas = reverse('api:raza-list')
    data = {
        'usuario': usuario,
        'tipo': tipo,
        'urlPost': nombre_url_creacion_mascota,
        'urlRaza': nombre_url_razas
    }

    return render(request, 'dashboard/crearMascota.html', data)

def mascota(request, id):
    mascota = MascotaUser.objects.get(id=id)
    usuario = UserProfile.objects.filter(user=request.user)
    data = {
        'mascota': mascota,
        'usuario': usuario
    }
    return render(request, 'dashboard/infoMascota.html', data)