from  tags.views import TagsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TagsViewSet)

urlpatterns = router.urls