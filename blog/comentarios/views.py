from rest_framework import viewsets
from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer
from publicaciones.models import Publicacion
from publicaciones.serializers import PublicacionSerializer
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response

# Create your views here.
class ComentariosViewSet(viewsets.ModelViewSet):
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()

    #agregar enpoint detalle comentarios/id_comentario/publicacion 
    @action(methods = ['GET'], detail = True)
    def detalle_publicacion(self, request, pk = None):
        comentario =  self.get_object()
        publicacion = Publicacion.objects.filter(id = comentario.publicacion_id)
        serializer = PublicacionSerializer(publicacion, many = True)
        return Response(status = status.HTTP_200_OK, data = serializer.data)


    
    