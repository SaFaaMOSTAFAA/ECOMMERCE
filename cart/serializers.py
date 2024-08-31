from rest_framework import serializers

from cart.models import Cart, CartItem
from products.serializers import ProductSerializer
from users.serializers import CustomerAccountSerializer


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = "__all__"


class ListCartItemSerializer(serializers.ModelSerializer):
    customeraccount = CustomerAccountSerializer()
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = "__all__"
