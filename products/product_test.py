import unittest
import json
from product import ProductProfile



class TestProductProfile(unittest.TestCase):
    def setUp(self):
        self.new_product = ProductProfile('P0001', "Test Product", 10, 50, 'Good product')

    def test_init(self):
        self.assertEqual(self.new_product.product_id, 'P0001')
        self.assertEqual(self.new_product.product_name, 'Test Product')
        self.assertEqual(self.new_product.quantity, 10)
        self.assertEqual(self.new_product.price, 50)
        self.assertEqual(self.new_product.description, 'Good product')

    def test_save_product_to_file(self):
        product_database = 'database/products.json'
        with open(product_database, 'r') as product_file:
            products = json.load(product_file)
            print(products)
            self.new_product.save_product()
            self.assertEqual(len(products), 1)

if __name__ == '__main__':
    unittest.main()