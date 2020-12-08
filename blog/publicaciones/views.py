from publicaciones.models import Publicacion
from publicaciones.serializers import PublicacionSerializer
from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer
from tags.models import Tag
from tags.serializers import TagSerializer
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response

# Create your views here.
class PublicacionesViewSet(viewsets.ModelViewSet):
    serializer_class = PublicacionSerializer
    queryset = Publicacion.objects.all()

    #serializar tags para obtener detalles
    @action(methods = ['GET'], detail = True)
    def mostrar_tags(self, request, pk = None):
        publicacion = self.get_object()
        serializer = TagSerializer(publicacion.tag, many = True)
        return Response(status = status.HTTP_200_OK, data = serializer.data)

    @action(methods = ['GET'], detail = True)
    def mostrar_comentarios(self, request, pk = None):
        #comentario = self.get_queryset().filter(publicacion  = pk, orderStatus=0)
        comentario = Comentario.objects.filter(publicacion = pk)
        serializer = ComentarioSerializer(comentario, many = True)
        return Response(status = status.HTTP_200_OK, data = serializer.data)
    
    

    

    
    
