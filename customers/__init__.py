from .customer import CustomerProfile
import json
customers_database = 'database/customers.json'

def create_customer():
    '''
    Create new customer
    '''
    print('********************')
    print('Enter requested detail to create a new customer account')
    name = input('''Enter customer name: ''')
    location = input('''Enter customer location: ''')
    contact = input('''Enter customer contact: ''')
    print('Creating customer account...')

    customer_account_info = CustomerProfile(customer_name = name, location = location, contact = contact)
    print('Please wait!! Saving to database...')
    CustomerProfile.save_customer(customer_account_info)
    print("Account for: " + customer_account_info.customer_name + " has been created successfully.")
    return customer_account_info


def display_all_customer_accounts():
    all_accounts = CustomerProfile.display_customer_accounts()
    print(all_accounts)