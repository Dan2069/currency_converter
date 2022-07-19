from unittest import TestCase
from app import app, my_convert, my_symbol

class ConvertTestCase(TestCase):
    def test_convert(self):
        ## Do i need to add a set up or tear down?
        self.assertEqual(my_convert('USD', 'GBP', 50), 42.24)
        self.assertEqual(my_convert('MXN', 'EUR', 36), 1.72)
        self.assertEqual(my_convert('AUD', 'PHP', 73), 2779.45)
    def test_symbol(self):
        self.assertEqual(my_symbol('USD', 'GBP'), ['$','£'])
        self.assertEqual(my_symbol('MXN', 'EUR'), ['$','€'])
        self.assertEqual(my_symbol('AUD', 'PHP'), ['$','₱'])
    

    def test_currency_form(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Convert Currencies!</h1>', html)

    def test_currency_submit(self):
        with app.test_client() as client:
            res = client.post('/convert', data={'convert_from': 'USD', 'convert_to': 'GBP', 'amount': '50'})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h2>$ 50 USD is £ 41.81 GBP</h2>', html)
