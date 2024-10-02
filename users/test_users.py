import pytest
from django.test import Client
from django.urls import reverse
from rest_framework_simplejwt.tokens import AccessToken

from users.models import Admin, Trader


@pytest.mark.django_db
class TestTraderAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.admin = Admin.objects.create(
            full_name='admin1', phone='01012070620',
            user_name='admin1', password='admin',
            email='admin1@gmail.com'
        )

        self.trader = Trader.objects.create(
            full_name='trader1', phone='01012070620',
            user_name='trader1', password='admin',
            email='trader1@gmail.com', address='address1'
        )
        self.client = Client()
        access_token = AccessToken.for_user(self.admin)
        self.client.defaults['HTTP_AUTHORIZATION'] = \
            f'Bearer {str(access_token)}'
        self.url_list = reverse("traders-list")
        self.url_detail = reverse("traders-detail", args=[self.trader.id])

    def test_list_trader(self):
        response = self.client.get(self.url_list)
        assert response.status_code == 200

    def test_create_trader(self):
        data = {
            'full_name': 'trader2', 'phone': '01012070620',
            'user_name': 'trader2', 'password': 'admin',
            'email': 'trader1@gmail.com', 'address': 'address2'
        }
        response = self.client.post(
            self.url_list, data=data, content_type='application/json'
        )
        assert response.status_code == 201

    def test_update_trader(self):
        update_data = {
            'full_name': 'trader_2', 'phone': '01012070620',
            'user_name': 'trader_2', 'password': 'trader',
            'email': 'trader1@gmail.com', 'address': 'address_2'
        }
        response = self.client.put(
            self.url_detail, data=update_data, content_type='application/json')
        assert response.status_code == 200

    def test_retrieve_trader(self):
        update_data = {
            'full_name': 'trader_2', 'phone': '01012070620',
            'password': 'admin', 'email': 'trader1@gmail.com',
            'user_name': 'trader_2', 'address': 'address_2'
        }
        response = self.client.get(
            self.url_detail,
            data=update_data,
            content_type='application/json'
        )
        assert response.status_code == 200

    def test_delete_trader(self):
        response = self.client.delete(
            self.url_detail
        )
        assert response.status_code == 204
