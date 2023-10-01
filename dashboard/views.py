from django.shortcuts import render, redirect, get_object_or_404
from aplicacion.models import MascotaUser, UserProfile

# Create your views here.
def dashboard(request):
    mascotas = MascotaUser.objects.filter(dueño=request.user)
    usuario = UserProfile.objects.filter(user=request.user)
    context = {
        'mascotas': mascotas,
        'usuario': usuario
    }
    return render(request, 'dashboard/base.html', context)

def mascota(request, id):
    mascota = MascotaUser.objects.get(id=id)
    usuario = UserProfile.objects.filter(user=request.user)
    data = {
        'mascota': mascota,
        'usuario': usuario
    }
    return render(request, 'dashboard/baseMascota.html', data)