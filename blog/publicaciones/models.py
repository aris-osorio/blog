from django.db import models
from tags.models import Tag

# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length = 200)
    nombre = models.CharField(max_length = 200)
    fecha  = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    texto = models.CharField(max_length = 200)

    tag = models.ManyToManyField(Tag, related_name='publicaciones')

    def __str__(self):
        return self.titulo