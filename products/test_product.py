import tempfile

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client
from django.urls import reverse
from PIL import Image

from products.models import Brand, Category, Product


@pytest.mark.django_db
class TestProducttAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.brand = Brand.objects.create(name='brand1')
        self.category = Category.objects.create(name='category1')
        with tempfile.NamedTemporaryFile(suffix='.png') as tmp:
            image = Image.new('RGB', (100, 100), color='red')
            image.save(tmp, format='PNG')
            tmp.seek(0)

            uploaded_image = SimpleUploadedFile(
                name='test_image.png', content=tmp.read(),
                content_type='image/png')

        self.product = Product.objects.create(
            name='product1', price='55.55', quantity='6',
            image=uploaded_image, purchase_price='66.55',
            category=self.category, brand=self.brand)
        print(f'this is product id {self.product.id}')
        self.client = Client()
        self.url_list = reverse("products-list")
        self.url_detail = reverse("products-detail", args=[self.product.id])

    def test_list_product(self):
        response = self.client.get(self.url_list)
        assert response.status_code == 200

    def test_create_product(self):
        with tempfile.NamedTemporaryFile(suffix='.png') as tmp:
            image = Image.new('RGB', (100, 100), color='red')
            image.save(tmp, format='PNG')
            tmp.seek(0)
            uploaded_image = SimpleUploadedFile(
                name='test_image.png', content=tmp.read(),
                content_type='image/png')
        data = {
            'name': 'product1', 'price': '55.55', 'quantity': '6',
            'image': uploaded_image, 'purchase_price': '66.55',
            'category': self.category.id, 'brand': self.brand.id
        }
        response = self.client.post(
            self.url_list, data=data, format='multipart')
        assert response.status_code == 201

    def test_update_product(self):
        with tempfile.NamedTemporaryFile(suffix='.png') as tmp:
            image = Image.new('RGB', (100, 100), color='red')
            image.save(tmp, format='PNG')
            tmp.seek(0)
            uploaded_image = SimpleUploadedFile(
                name='test_image.png', content=tmp.read(),
                content_type='image/png')
        update_data = {
            'name': 'product1', 'price': '58.55', 'quantity': '8',
            'image': uploaded_image, 'purchase_price': '66.55'
        }
        response = self.client.patch(self.url_detail,
                                     data=update_data, format='multipart')
        assert response.status_code == 200

    def test_delete_product(self):
        response = self.client.delete(self.url_detail)
        print(response.data)
        assert response.status_code == 204
