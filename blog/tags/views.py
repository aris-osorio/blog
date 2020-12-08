from rest_framework.decorators import action
from rest_framework import viewsets
from tags.models import Tag
from tags.serializers import TagSerializer
from publicaciones.models import Publicacion
from publicaciones.serializers import PublicacionSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

# Create your views here.
class TagsViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    @action(methods = ['GET'], detail = True)
    def mostrar_publicaciones(self, request, pk = None):
        tag = self.get_object()
        serializer = PublicacionSerializer(tag.publicaciones, many = True)
        return Response(status = status.HTTP_200_OK, data = serializer.data)