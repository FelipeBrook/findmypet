from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import geocoder  # Importa la biblioteca para obtener la ubicación
import qrcode
from django.contrib import messages
from django.contrib.auth.decorators import login_required #ocultar la vista si no esta logeado
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from geopy.geocoders import Nominatim
import googlemaps
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from .models import Producto
from .models import Mascota
from .Carrito import Carrito  # Importar la clase Carrito desde carrito.py
from django.http import HttpResponseRedirect





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



def perfil_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)

    # Obtiene la dirección IP del usuario
    usuario_ip = get_client_ip(request)

    # Configura el cliente de Google Maps con tu clave de API
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    try:
       
        # Utiliza la función geolocate para obtener una ubicación precisa
        location = gmaps.geolocate()

        latitud = location['location']['lat']
        longitud = location['location']['lng']

        # Obtiene la dirección precisa a partir de las coordenadas
        ubicacion = gmaps.reverse_geocode((latitud, longitud))

        # Ubicación será una lista de resultados; puedes elegir el que mejor se ajuste a tus necesidades
        ubicacion = ubicacion[0]['formatted_address']
    except Exception as e:
        ubicacion = "Ubicación desconocida"

    # Crear el código QR con la información del perfil de la mascota
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Puedes ajustar la URL a tu vista de perfil de mascota
    qr.add_data(f'http://127.0.0.1:8000/mascotas/{mascota_id}/')
    
    qr.make(fit=True)

    # Crear una imagen del código QR
    img = qr.make_image(fill_color="black", back_color="white")

    # Construye el nombre de archivo con el número de la mascota
    nombre_archivo = f"codigo_qr_mascota_{mascota_id}.png"

    # Guardar la imagen del código QR en el servidor
    img.save(nombre_archivo)

    # Registra la ubicación en la base de datos
    mascota.ubicacion_escaneo = ubicacion  # Puedes ajustar esto según tus necesidades
    mascota.save()

    # Renderizar la plantilla HTML y pasar la imagen del código QR, la mascota y la ubicación
    return render(request, 'aplicacion/perfil_mascota.html', {'mascota': mascota, 'qr_image': img, 'ubicacion': ubicacion})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip




def home(request):
    return render(request, "aplicacion/home.html")
def contacto(request):
    return render(request, "aplicacion/contacto.html")
def login(request):
    return render(request, "aplicacion/login.html")
def lugares(request):
    return render(request, "aplicacion/lugares.html")
def sobremi(request):
    return render(request, "aplicacion/sobremi.html")
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


# views.py
#ECOMMERCE

def carrito(request):
    return render(request, "aplicacion/carrito.html")

def ecommerce(request):
    productos = Producto.objects.all()
    return render(request, "aplicacion/ecommerce.html", {'productos': productos})


# def agregar_producto(request, producto_id):
#     carrito = Carrito(request)
#     producto = Producto.objects.get(id=producto_id)
#     carrito.agregar(producto)
#     return redirect("ecommerce")

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    
    # Obtener la URL de la página anterior (URL referer)
    redirect_to = request.META.get('HTTP_REFERER', '/')
    
    # Verificar la URL para decidir a dónde redirigir
    if 'carrito' in redirect_to:
        # Si la URL contiene 'carrito', permanecer en la página 'carrito'
        return HttpResponseRedirect(redirect_to)
    elif 'ecommerce' in redirect_to:
        # Si la URL contiene 'ecommerce', permanecer en la página 'ecommerce'
        return HttpResponseRedirect(redirect_to)



def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")


