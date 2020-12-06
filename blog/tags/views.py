from rest_framework.decorators import action
from rest_framework import viewsets
from tags.models import Tag
from tags.serializers import TagSerializer

# Create your views here.
class TagsViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()