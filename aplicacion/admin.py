from django.contrib import admin
from .models import Contacto,Mascota




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



# Register your models here.
