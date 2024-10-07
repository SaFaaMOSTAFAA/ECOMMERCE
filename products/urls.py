from django.urls import path
from rest_framework.routers import DefaultRouter

from products.api import (BrandApiViwe, BrandListApiView, CategoryViewSet,
                          ProductReviewViewSet, ProductViewSet,
                          WishListViewSet)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename="categories")
router.register(r'products', ProductViewSet, basename="products")
router.register(r'product-reviews',
                ProductReviewViewSet, basename="product-reviews")
router.register(r'wish-lists', WishListViewSet, basename="wish-lists")

urlpatterns = router.urls
urlpatterns += [
    path('brands/', BrandListApiView.as_view()),
    path('brands/<int:pk>/', BrandApiViwe.as_view()),

]
