import pytest
from django.test import Client
from django.urls import reverse

from cart.models import Cart, CartItem
from products.models import Brand, Category, Product
from users.models import CustomerAccount


@pytest.mark.django_db
class TestCartAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.customeraccount = CustomerAccount.objects.create(
            full_name='customer1', phone='01012070620', user_name='customer1',
            password='admin', email='customer1@gmail.com', address='address1')
        self.cart = Cart.objects.create(customer=self.customeraccount)
        self.client = Client()
        self.url_list = reverse("cart-list")
        self.url_detail = reverse("cart-detail", args=[self.cart.id])

    def test_list_cart(self):
        response = self.client.get(self.url_list)
        assert response.status_code == 200

    def test_create_cart(self):
        data = {
            'customer': self.customeraccount.id
        }
        response = self.client.post(self.url_list,
                                    data=data,
                                    content_type='application/json')
        assert response.status_code == 201

    def test_retrieve_cart(self):
        response = self.client.get(self.url_detail,
                                   content_type='application/json')
        assert response.status_code == 200

    def test_delete_cart(self):
        response = self.client.delete(self.url_detail)
        assert response.status_code == 204


@pytest.mark.django_db
class TestCartItemAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.customeraccount = CustomerAccount.objects.create(
            full_name='customer1', phone='01012070620', user_name='customer1',
            password='admin', email='customer1@gmail.com', address='address1')
        self.cart = Cart.objects.create(customer=self.customeraccount)
        self.category = Category.objects.create(name='category1')
        self.brand = Brand.objects.create(name='brand1')
        self.product = Product.objects.create(
            name='product1', price='22.55', quantity='5',
            image='ecommerce.jpg', purchase_price='44.66',
            category=self.category, brand=self.brand)
        self.cartitem = CartItem.objects.create(
            product_cost='55.99', product=self.product, cart=self.cart)
        self.client = Client()
        self.url_list = reverse("cart-items-list")
        self.url_detail = reverse("cart-items-detail", args=[self.cartitem.id])

    def test_list_catritem(self):
        response = self.client.get(self.url_list)
        assert response.status_code == 200

    def test_create_cartitem(self):
        data = {
            'product_cost': '55.99',
            'product': self.product.id,
            'cart': self.cart.id
        }
        response = self.client.post(self.url_list,
                                    data=data,
                                    content_type='application/json')
        assert response.status_code == 201

    def test_update_cartitem(self):
        update_data = {
            'product_cost': '66.99',
            'product': self.product.id,
            'cart': self.cart.id
        }
        response = self.client.put(self.url_detail,
                                   data=update_data,
                                   content_type='application/json')
        assert response.status_code == 200

    def test_test_retrieve_cartitem(self):
        update_data = {
            'product_cost': '69.99',
            'product': self.product.id,
            'cart': self.cart.id
        }
        response = self.client.patch(self.url_detail,
                                     data=update_data,
                                     content_type='application/json')
        assert response.status_code == 200

    def test_delete_cartitem(self):
        response = self.client.delete(
            self.url_detail, )
        assert response.status_code == 204
