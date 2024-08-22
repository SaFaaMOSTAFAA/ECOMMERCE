from rest_framework.routers import DefaultRouter

from users.api import AdminViewSet, TraderViewSet

router = DefaultRouter()
router.register(r'admins', AdminViewSet, basename="admins")
router.register(r'traders', TraderViewSet, basename="traders")

urlpatterns = router.urls
