import json
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
        self.new_customer = CustomerProfile('Numero Uno','Kimperria', 'Nairobi', 123)

    def test_init(self):
        '''
        Test if the object is initialized properly
        '''
        self.assertEqual(self.new_customer.customer_id, 'Numero Uno')
        self.assertEqual(self.new_customer.customer_name, "Kimperria")
        self.assertEqual(self.new_customer.location, 'Nairobi')
        self.assertEqual(self.new_customer.contact, 123)

    def test_save_customer_info(self):
        '''
        Test if new customer object is saved to the customer database
        '''
        customers_database = 'database/customers.json'
        with open(customers_database, 'r') as customers_file:
            customer_accounts = json.load(customers_file)
        self.new_customer.save_customer()
        self.assertEqual(len(customer_accounts), 1)
    
    # def tearDown(self):
    #     '''
    #     Clean up customer list
    #     '''
    #     CustomerProfile.customers_list = []

    # def test_save_multiple_customers(self):
    #     '''
    #     Test if it can save multiple customers info
    #     '''
    #     self.new_customer.save_customer()
    #     test_customer = CustomerProfile('Customer2', 'Kigali', 123)
    #     test_customer.save_customer()
    #     self.assertEqual(len(CustomerProfile.customers_list), 2)

    # def test_delete_customer_info(self):
    #     '''
    #     Test if customer can be deleted
    #     '''
    #     self.new_customer.save_customer()
    #     delete_customer = CustomerProfile('Ranger', 'Savannah', 123)
    #     delete_customer.save_customer()
    #     self.new_customer.delete_customer()
    #     self.assertEqual(len(CustomerProfile.customers_list), 1)
    
    # def test_search_customer_by_name(self):
    #     '''
    #     Search customer in list by name
    #     '''
    #     self.new_customer.save_customer()
    #     find_customer = CustomerProfile('Alien', 'Space', 789)
    #     find_customer.save_customer()
    #     found_customer = CustomerProfile.search_customer_by_name('Alien')
    #     self.assertEqual(found_customer.location, find_customer.location)

    # def test_customer_exists(self):
    #     '''
    #     Test to check if customer account already exists
    #     '''

    #     self.new_customer.save_customer()
    #     check_account = CustomerProfile('Kim', 'Nakuru', 123)
    #     check_account.save_customer()

    #     customer_exist = CustomerProfile.customer_exist('Kim')
    #     self.assertTrue(customer_exist)

    # def test_display_all_customers(self):
    #     '''
    #     Show all accounts
    #     '''
    #     self.assertEqual(CustomerProfile.display_customer_accounts(), CustomerProfile.customers_list)

if __name__ == '__main__':
    unittest.main()