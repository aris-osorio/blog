from publicaciones.views import PublicacionesViewSet
from rest_framework import renderers

publicaciones_list = PublicacionesViewSet.as_view({
    'get': 'list',
    'post': 'create'
})