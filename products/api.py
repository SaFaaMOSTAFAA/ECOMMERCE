from rest_framework.viewsets import ModelViewSet

from products.models import Category, Product, ProductReview, WishList
from products.serializers import (CategorySerializer,
                                  ListProductReviewSerializer,
                                  ListProductSerializer,
                                  ListWishListSerializer,
                                  ProductReviewSerializer, ProductSerializer,
                                  WishListSerializer)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.order_by('-id')
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.order_by('-id').select_related('category')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListProductSerializer
        return ProductSerializer


class ProductReviewViewSet(ModelViewSet):
    queryset = ProductReview.objects.order_by('-id').select_related(
        'product', 'customer')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListProductReviewSerializer
        return ProductReviewSerializer


class WishListViewSet(ModelViewSet):
    queryset = WishList.objects.order_by('-id').select_related(
        'product', 'customer')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListWishListSerializer
        return WishListSerializer
