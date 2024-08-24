from rest_framework.viewsets import ModelViewSet

from products.models import Category, Product
from products.serializers import (CategorySerializer, ListProductSerializer,
                                  ProductSerializer)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListProductSerializer
        return ProductSerializer
