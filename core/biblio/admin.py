from django.contrib import admin
from biblio.models import *

class UserAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('Nombre', 'Direccion', 'Telefono',)
        }),
        ('Detalle de alquileres', {
            'fields': ('Ejemplares',)
        }),
    )

    list_display = ['Nombre', 'Telefono']

# Register your models here.
admin.site.register(Autor,)
admin.site.register(Libro,)
admin.site.register(Ejemplar,)
admin.site.register(Usuario, UserAdmin)
