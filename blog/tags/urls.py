from tags.views import TagsViewSet
from rest_framework import renderers

tags_list = TagsViewSet.as_view({
    'get': 'list',
    'post': 'create',
})