from rest_framework.routers import DefaultRouter

from products.api import CategoryViewSet, ProductReviewViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename="categories")
router.register(r'products', ProductViewSet, basename="products")
router.register(r'product-reviews',
                ProductReviewViewSet, basename="product-reviews")

urlpatterns = router.urls
