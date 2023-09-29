from django.shortcuts import render,redirect
from .forms import CoctactoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required #ocultar la vista si no esta logeado
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from .forms import CustomUserCreationForm
# from django.contrib.auth import authenticate, login
# from .forms import LoginForm
from django.contrib.auth import logout

# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html")
def contacto(request):
    return render(request, "aplicacion/contacto.html")
def login(request):
    return render(request, "aplicacion/login.html")
# def register(request):
#     return render(request, "aplicacion/register.html")
def signup_view(request):
    return render(request, 'account/signup.html')
@login_required
def pet(request):
    return render(request, "aplicacion/pet.html")

def contacto(request):
    data={
        'form':CoctactoForm()
    }
    if request.method=='POST':
        formulario=CoctactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Contacto guardado correctamente")
           
            
        else:
            data["form"]=formulario
    return render(request, "aplicacion/contacto.html", data)


# def register(request):
#     data = {
#         'form': CustomUserCreationForm()
#         }
#     if request.method=='POST':
#         user_creation_form=CustomUserCreationForm(data=request.POST)
#         if user_creation_form.is_valid():
#             user_creation_form.save()
#             messages.success(request, "Registro completado exitosamente")
#             user =authenticate(username=user_creation_form.cleaned_data["username"], password=user_creation_form.cleaned_data["password1"])
            
#             return redirect(to='login')
        
            
        
#     return render(request, "aplicacion/register.html", data)
  
def exit(request):
    logout(request)
    return redirect('home')



