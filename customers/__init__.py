from .customer import CustomerProfile

def create_customer():
    '''
    Create new customer
    '''
    print('********************')
    print('Enter requested detail to create a new customer account')
    name = input('''Enter customer name: ''')
    location = input('''Enter customer location: ''')
    contact = input('''Enter customer contact: ''')

    customer_account_info = CustomerProfile(customer_name = name, location = location, contact = contact)
    print(customer_account_info)

create_customer()