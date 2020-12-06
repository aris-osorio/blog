from rest_framework.decorators import action
from rest_framework import viewsets
from publicaciones.models import Publicacion
from publicaciones.serializers import PublicacionSerializer

# Create your views here.
class PublicacionesViewSet(viewsets.ModelViewSet):
    serializer_class = PublicacionSerializer
    queryset = Publicacion.objects.all()
    
    
