from django.shortcuts import render
from .forms import CoctactoForm,petForm
from django.contrib import messages
import qrcode
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html")
def contacto(request):
    return render(request, "aplicacion/contacto.html")
def login(request):
    return render(request, "aplicacion/login.html")

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

def pet(request):
    data={
        'form':petForm()
    }
    if request.method=='POST':
        formulario=petForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "compañero guardado correctamente")
           
            
        else:
            data["form"]=formulario
    return render(request, "aplicacion/pet.html", data)

def mostrar_qr(request, pk):
    # Obtén la mascota desde la base de datos o de donde la hayas almacenado
    mascota = get_object_or_404(pet, pk=pk)

    # Crea el contenido para el código QR con la información de la mascota
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"Nombre: {mascota.nombre}\nEspecie: {mascota.especie}\nRaza: {mascota.raza}")
    qr.make(fit=True)

    # Crea una imagen del código QR
    img = qr.make_image(fill_color="black", back_color="white")

    # Almacena la imagen en un objeto BytesIO
    image_io = BytesIO()
    img.save(image_io, format='PNG')

    # Crea un archivo de imagen en memoria
    qr_image = InMemoryUploadedFile(image_io, None, f'qr_{mascota.nombre}.png', 'image/png', image_io.tell(), None)

    # Guarda la imagen en el directorio de medios
    mascota.qr_code = qr_image
    mascota.save()

    return render(request, 'mostrar_qr.html', {'mascota': mascota})





