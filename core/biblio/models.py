from django.db import models

# Create your models here.

class Autor(models.Model):
    Nombre = models.CharField(max_length=50)
    Codigo = models.AutoField(primary_key=True)

    def __str__(self):
        return ("{} : {}".format(self.Codigo, self.Nombre))

class Libro(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=30)
    Paginas = models.IntegerField()
    Editorial = models.CharField(max_length=40)
    Autor = models.ForeignKey('Autor', on_delete=models.CASCADE, null=True,)

    def __str__(self):
        return ("{} : {}".format(self.Codigo, self.Titulo))

class Ejemplar(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Localizacion = models.CharField(max_length=30)
    Libro = models.ForeignKey('Libro', on_delete=models.CASCADE, null=True,)

    def __str__(self):
        return ("{} : {}: Libro:{}".format(self.Codigo, self.Localizacion, self.Libro))
