from .customer import CustomerProfile
import json
customers_database = 'database/customers.json'

def read_customer_database():
    '''
    Function to read customers database
    '''
    with open(customers_database, 'r') as customers_file:
        customers = json.load(customers_file)
        return customers
       

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
    try:
        CustomerProfile.save_customer(name, location, contact)
    except:
        print("Unable to create customer")

def search_customer_by_name():
    name = input("Enter name: ")
    found = CustomerProfile.customer_exist(name)
    print(found)
    CustomerProfile.search_customer_by_name(name)

def search_customer_by_id():
    customer_id = input("Enter customer account ID: ")
    found = CustomerProfile.customer_exist_by_id(customer_id)
    if found == True:
        customer = CustomerProfile.search_customer_by_id(customer_id)
        print('**************')
        print('Customer Account Found')
        print('**************')
        print(customer)
        print('**************')
    elif found == False:
        print('**************')
        print('Customer account with such ID does not exist')
        print('**************')


def display_all_customer_accounts():
    '''
    Show all customer accounts
    '''
    CustomerProfile.show_all_customers()


def update_customer_account():
    '''
    Update customer account information
    '''
    id = input("Enter customer ID: ")
    state = CustomerProfile.customer_exist_by_id(id)
    if state == True:
        customer_name = input("Enter new name: ")
        customer_location = input("Enter new location: ")
        customer_contact = input('Enter new contact information: ')
        CustomerProfile.update_customer_account(customer_id=id, customer_name=customer_name, location = customer_location, contact = customer_contact)
    elif state == False:
        print("Customer with that ID does not exist")
        print("Please try again!")
        update_customer_account()
    else:
        print("An error occured. Please contact Admin")

def delete_customer_account():
    '''
    Delete account by name
    '''
    customer_account_name = input('Enter customer name: ')
    account_exist = CustomerProfile.customer_exist(customer_account_name)
    if account_exist == True:
        CustomerProfile.search_customer_by_name(customer_account_name)
        print('Are you sure you want to delete ' + str(customer_account_name) + '\'s account?')
        print('This account information will forever be lost!!!')
        print('''Enter ID to delete account 
        or 
Enter 00 to exit''')
        id = input("Enter customer ID: ")
        danger = 0 
        while danger != "0":
            danger = input("Type 1 to confirm action!")
            if danger == "1":
                CustomerProfile.delete_customer(id)
                print(f"{customer_account_name}'s Account has been deleted!")
            elif danger == "00":
                delete_customer_account()
            break
    elif account_exist == False:
        print('Seems the account you searched for does not exist')