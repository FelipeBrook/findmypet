from django.contrib import admin
from .models import Contacto,Mascota, TipoMascota, RazaMascota, MascotaUser, UserProfile


class RazaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_mascota']
    search_fields = ['nombre']
    list_filter = ['tipo_mascota']

class MascotasAdmin2(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'raza', 'dueño']
    search_fields = ['nombre', 'dueño']
    list_filter = ['tipo']

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
admin.site.register(MascotaUser, MascotasAdmin2)
admin.site.register(UserProfile)
admin.site.register(TipoMascota)
admin.site.register(RazaMascota, RazaAdmin)



# Register your models here.
