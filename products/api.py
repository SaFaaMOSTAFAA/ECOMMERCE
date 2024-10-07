from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from products.models import Brand, Category, Product, ProductReview, WishList
from products.serializers import (BrandSerializer, CategorySerializer,
                                  ListProductReviewSerializer,
                                  ListProductSerializer,
                                  ListWishListSerializer,
                                  ProductReviewSerializer, ProductSerializer,
                                  WishListSerializer)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.order_by('-id')
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.order_by('-id').select_related(
        'category', 'brand')

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


class BrandListApiView(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        page_pagin = PageNumberPagination()
        page_pagin.page_size = 10
        pagin_brand = page_pagin.paginate_queryset(brands, request)
        serialize = BrandSerializer(pagin_brand, many=True)
        return page_pagin.get_paginated_response(serialize.data)

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class BrandApiViwe(APIView):

    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        brands = self.get_object(pk)
        serializer = BrandSerializer(brands, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        brands = self.get_object(pk)
        serializer = BrandSerializer(brands, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        brands = self.get_object(pk)
        brands.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
