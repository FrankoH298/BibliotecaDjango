from django.contrib import admin
from biblio.models import *

class EntryInLines(admin.TabularInline):
    model = Libro

class AuthorAdmin(admin.ModelAdmin):
    inlines = [EntryInLines,]
    search_fields = ('Nombre',)

class EjemplarAdmin(admin.ModelAdmin):
    list_display = ('Libro',)
    
class LibroAdmin(admin.ModelAdmin):
    list_display = ('Titulo', 'Editorial',)


class EntryFilter(admin.SimpleListFilter):
    title = 'mayoria de edad'
    parameter_name = 'Edad'

    def lookups(self, request, model_admin):
        return (
            # Dependiendo lo que seleccionemos nos devuelve un valor
            ('+18', ("Mayor de edad")),
            ('-18', ('Menor de edad')),
        )

    def queryset(self, request, queryset):
        # Dependiendo del valor nos retorna algo
        if self.value() == '+18':
            # gte = greater then or equals
            return queryset.filter(Edad__gte = 18)
        elif self.value() == '-18':
            # lt = less then
            return queryset.filter(Edad__lt = 18)

class UserAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('Datos', {
            'fields': ('Nombre', 'Edad')
        }),
        ('Contacto', {
            'fields': ('Direccion', 'Telefono',)
        }),
    )

    # Datos a mostrar
    list_display = ('Nombre', 'Telefono', 'Edad', 'adults', 'color', )
    # Datos que son clickeables
    list_display_links = ('Nombre', 'Telefono',)
    
    filter_horizontal = ('Ejemplares',)

    # Permite buscar por dato
    search_fields = ('Nombre',)

    # Permite filtrar por dato
    list_filter = (EntryFilter,)
    
    actions = ('')
    """
    def make_published(self, request, queryset):
        return queryset.update(published = True)
    make_published.short_description = 'Cambiar a publicado'
    """
    
# Register your models here.
admin.site.register(Autor, AuthorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Usuario, UserAdmin)
