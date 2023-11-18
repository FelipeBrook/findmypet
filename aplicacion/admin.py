from django.contrib import admin
from .models import Mascota, Raza, Marca, Alimentos




# class ContactoAdmin(admin.ModelAdmin):
#     list_display = ["nombre","correo","telefono",]
#     list_editable = ["correo","telefono"]
#     search_fields = ["nombre","correo","telefono"]
#     list_filter = ["nombre","correo","telefono"]
   




# Register your models here.
admin.site.register(Mascota)
admin.site.register(Raza)
admin.site.register(Marca)
admin.site.register(Alimentos)