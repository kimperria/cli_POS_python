import unittest
from customer import CustomerProfile


class TestCustomer(unittest.TestCase):
    '''
    Test class for customer class behaviours
    '''

    def setUp(self):
        '''
        Set up new customer objects before each case
        '''
        self.new_customer = CustomerProfile('Kimperria', 'Nairobi', 123)

    def test_init(self):
        '''
        Test if the object is initialized properly
        '''
        self.assertEqual(self.new_customer.customer_name, "Kimperria")
        self.assertEqual(self.new_customer.location, 'Nairobi')
        self.assertEqual(self.new_customer.contact, 123)

    def test_save_customer_info(self):
        '''
        Test if new customer object is saved to the customer list
        '''
        self.new_customer.save_customer()
        self.assertEqual(len(CustomerProfile.customers_list), 1)
    
    def tearDown(self):
        '''
        Clean up customer list
        '''
        CustomerProfile.customers_list = []

    def test_save_multiple_customers(self):
        '''
        Test if it can save multiple customers info
        '''
        self.new_customer.save_customer()
        test_customer = CustomerProfile('Customer2', 'Kigali', 123)
        test_customer.save_customer()
        self.assertEqual(len(CustomerProfile.customers_list), 2)

    def test_delete_customer_info(self):
        '''
        Test if customer can be deleted
        '''
        self.new_customer.save_customer()
        delete_customer = CustomerProfile('Ranger', 'Space', 123)
        delete_customer.save_customer()
        self.new_customer.delete_customer()
        self.assertEqual(len(CustomerProfile.customers_list), 1)

if __name__ == '__main__':
    unittest.main()