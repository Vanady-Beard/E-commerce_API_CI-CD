import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_get_products(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_get_orders(self):
        response = self.app.get('/orders')
        self.assertEqual(response.status_code, 200)

    def test_get_order_items(self):
        response = self.app.get('/order_items')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

