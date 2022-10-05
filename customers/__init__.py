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
    CustomerProfile.update_customer_account(id)

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
                print("Account has been deleted!")
            elif danger == "00":
                delete_customer_account()
            break
    elif account_exist == False:
        print('Seems the account you searched for does not exist')


def search_customer_by_name():
    name = input("Enter name: ")
    CustomerProfile.search_customer_by_name(name)


