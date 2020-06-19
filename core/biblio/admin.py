from django.contrib import admin
from biblio.models import *

class EntryInLines(admin.TabularInline):
    model = Libro

class AuthorAdmin(admin.ModelAdmin):
    inlines = [EntryInLines,]
    search_fields = ['Nombre',]

class EjemplarAdmin(admin.ModelAdmin):
    list_display = ['Libro',]
    
class LibroAdmin(admin.ModelAdmin):
    list_display = ['Titulo', 'Editorial',]
    
class UserAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('Datos', {
            'fields': ('Nombre',)
        }),
        ('Contacto', {
            'fields': ('Direccion', 'Telefono',)
        }),
    )

    list_display = ['Nombre', 'Telefono', 'Edad', 'adults', 'color', ]
    list_display_links = ['Nombre', 'Telefono',]
    filter_horizontal = ('Ejemplares',)
    
    
# Register your models here.
admin.site.register(Autor, AuthorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Usuario, UserAdmin)
