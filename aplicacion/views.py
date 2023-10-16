from django.shortcuts import render,redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required #ocultar la vista si no esta logeado
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from . models import Mascota

@login_required
def adoptame(request):
    mascotas = Mascota.objects.all()
    data = {
        'mascotas':mascotas
    }
    return render(request, "aplicacion/adoptame.html", data)

def perfil_mascota(request, mascota_id):
    mascota = Mascota.objects.get(id=mascota_id)
    return render(request, 'aplicacion/perfil_mascota.html', {'mascota': mascota})



def home(request):
    return render(request, "aplicacion/home.html")
def contacto(request):
    return render(request, "aplicacion/contacto.html")
def login(request):
    return render(request, "aplicacion/login.html")
def lugares(request):
    return render(request, "aplicacion/lugares.html")

def signup_view(request):
    return render(request, 'account/signup.html')

@login_required
def pet(request):
    return render(request, "aplicacion/pet.html")
def perfiles(request):
    return render(request, "aplicacion/perfiles.html")

  
def exit(request):
    logout(request)
    return redirect('home')




