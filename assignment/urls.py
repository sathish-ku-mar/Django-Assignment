from .views import AdultViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', AdultViewSet, basename='api')
urlpatterns = router.urls