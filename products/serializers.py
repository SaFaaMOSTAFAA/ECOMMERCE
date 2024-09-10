from rest_framework import serializers

from products.models import Category, Product, ProductReview, WishList
from users.serializers import CustomerAccountSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ListProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductReview
        fields = "__all__"


class ListProductReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    customer_account = CustomerAccountSerializer()

    class Meta:
        model = ProductReview
        fields = "__all__"


class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishList
        fields = "__all__"


class ListWishListSerializer(serializers.ModelSerializer):
    customer = CustomerAccountSerializer()
    product = ProductSerializer()

    class Meta:
        model = WishList
        fields = "__all__"
