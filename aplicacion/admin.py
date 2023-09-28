from django.contrib import admin
from .models import Contacto,Mascota, TipoMascota, RazaMascota


class RazaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_mascota']
    search_fields = ['nombre']
    list_filter = ['tipo_mascota']

class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre","correo","telefono",]
    list_editable = ["correo","telefono"]
    search_fields = ["nombre","correo","telefono"]
    list_filter = ["nombre","correo","telefono"]
   

class MascotaAdmin(admin.ModelAdmin):
    list_display = ["nombre","raza","edad"]
    list_editable = ["raza","edad"]
    search_fields = ["nombre","raza","edad"]
    list_filter = ["nombre","raza","edad"]


        
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Mascota,MascotaAdmin)
admin.site.register(TipoMascota)
admin.site.register(RazaMascota, RazaAdmin)



# Register your models here.
