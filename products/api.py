from rest_framework.viewsets import ModelViewSet

from products.models import Category, Product, ProductReview
from products.serializers import (CategorySerializer,
                                  ListProductReviewSerializer,
                                  ListProductSerializer,
                                  ProductReviewSerializer, ProductSerializer)


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
