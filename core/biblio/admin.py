from django.contrib import admin
from biblio.models import *

class EntryInLines(admin.TabularInline):
    model = Libro

class AuthorAdmin(admin.ModelAdmin):
    inlines = [EntryInLines,]

class EjemplarAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('Nombre', 'Direccion', 'Telefono', 'Edad',)
        }),
        ('Detalle de alquileres', {
            'fields': ('Ejemplares',)
        }),
    )

    list_display = ['Nombre', 'Telefono', 'Edad', 'adults', 'color', ]
    list_display_links = ['Nombre', 'Telefono',]
    filter_horizontal = ('Ejemplares',)
    
    
# Register your models here.
admin.site.register(Autor, AuthorAdmin)
admin.site.register(Libro,)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Usuario, UserAdmin)
