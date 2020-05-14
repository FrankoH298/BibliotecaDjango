from django.db import models

# Create your models here.

class Autor(models.Model):
    Nombre = models.CharField(max_length=50)
    Codigo = models.IntegerField(primary_key=True)

    def __str__(self):
        return ("{} : {}".format(self.Codigo, self.Nombre))

class Libro(models.Model):
    Codigo = models.IntegerField(primary_key=True)
    Titulo = models.CharField(max_length=30)
    Paginas = models.IntegerField()
    Editorial = models.CharField(max_length=40)
    Autor = models.ForeignKey('Autor', on_delete=models.CASCADE, null=True,)

    def __str__(self):
        return ("{} : {}".format(self.Codigo, self.Titulo))
