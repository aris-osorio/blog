from comentarios.views import ComentariosViewSet
from rest_framework import renderers

comentarios_list = ComentariosViewSet.as_view({
    'get': 'list',
    'post': 'create'
})