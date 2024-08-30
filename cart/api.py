from rest_framework.viewsets import ModelViewSet

from cart.models import Cart, CartItem
from cart.serializers import (CartItemSerializer, CartSerializer,
                              ListCartItemSerializer)


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListCartItemSerializer
        return CartItemSerializer
