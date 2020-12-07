from publicaciones.views import PublicacionesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PublicacionesViewSet)

urlpatterns = router.urls