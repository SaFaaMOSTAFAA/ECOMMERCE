from rest_framework.routers import DefaultRouter

from products.api import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename="categories")
router.register(r'products', ProductViewSet, basename="products")

urlpatterns = router.urls
