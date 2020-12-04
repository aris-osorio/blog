from django.db import models
from publicaciones.models import Publicacion

# Create your models here.
class Comentario(models.Model):
    nombre = models.CharField(max_length = 200)
    fecha  = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    texto = models.CharField(max_length = 200)

    publicacion = models.ForeignKey(Publicacion, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre