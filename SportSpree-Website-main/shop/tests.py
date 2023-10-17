from django.test import Client, TestCase
from django.urls import reverse
from .models import Product,Category


class ShopModelTests(TestCase):
    def setUp(self):
        self.c = Category.objects.create(name='Shoes')
        self.product = Product.objects.create(name='AIR JORDAN 1 HIGH OG', category=self.c, stock='87',
                                              price='100.00')
    def test_product_listing(self):
        self.assertEqual(f'{self.product.name}','AIR JORDAN 1 HIGH OG')
        self.assertEqual(f'{self.product.price}','100.00')
        self.assertEqual(f'{self.product.stock}','87')

    def test_product_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response, 'AIR JORDAN 1 HIGH OG')
        self.assertTemplateNotUsed(response, 'shop/category.html' )
    
    def test_product_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get('/1/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'AIR JORDAN 1 HIGH OG')
        self.assertTemplateUsed(response, 'shop.product.html')

