from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Autor(models.Model):
    Nombre = models.CharField(max_length=50)
    Codigo = models.AutoField(primary_key=True)

    def __str__(self):
        return ("{}".format(self.Nombre))
        

class Libro(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=30)
    Paginas = models.IntegerField()
    Editorial = models.CharField(max_length=40)
    Autor = models.ForeignKey('Autor', on_delete=models.CASCADE, null=True,)

    def __str__(self):
        return ("{}".format(self.Titulo))

class Ejemplar(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Localizacion = models.CharField(max_length=30)
    Libro = models.ForeignKey('Libro', on_delete=models.CASCADE, null=True,)
    Usuarios = models.ManyToManyField('Usuario',)

    def __str__(self):
        return ("Libro:{}".format(self.Libro))

class Usuario(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=20)
    Telefono = models.BigIntegerField()
    Direccion = models.CharField(max_length=40)
    Ejemplares = models.ManyToManyField('Ejemplar',)
    Edad = models.IntegerField()
    
    def adults(self):
        # Devuelve si es mayor o menor de edad
        return (self.Edad > 17)
    adults.boolean = True
    adults.short_description = 'Es mayor'
    
    # Nos devuelve un texto con color
    def color(self):
        if self.adults():
            return mark_safe("<b style='color:green;'>Aprobado</b>")
        else:
            return mark_safe("<b style='color:red;'>Desaprobado</b>")
    color.short_description = 'Adulto'
    
    def __str__(self):
        return ("{}".format(self.Nombre))
