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



def create_customer_id():
    '''
    Create new for every customer class instance
    '''
    customers = read_customer_database()
    id = 0
    for customer in customers:
        id = id + 1
        customer_id = "C000" + str(id)
        return customer_id
        

def create_customer():
    '''
    Create new customer
    '''
    print('********************')
    print('Enter requested detail to create a new customer account')
    customer_id = create_customer_id()
    print(customer_id)
    customer_account_info = {}
    data = read_customer_database()
    customer_account_info["customerId"] = customer_id
    customer_account_info["customerAccount"] = {}
    print('list', data)
    print(customer_account_info)
    name = input('''Enter customer name: ''')
    location = input('''Enter customer location: ''')
    contact = input('''Enter customer contact: ''')
    print('Creating customer account...')
    new_customer = CustomerProfile(customer_name = name, location = location, contact = contact)
    #serialize class instance as an object
    customer_account_info["customerAccount"] = json.dumps(new_customer.__dict__)
    print('new object', customer_account_info)
    data.append(customer_account_info)
    print('Please wait!! Saving to database...')
    with open(customers_database, 'w') as customers_file:
        json.dump(data, customers_file, indent=4)





def display_all_customer_accounts():
    '''
    Show all customer accounts
    '''
    all_accounts = CustomerProfile.display_customer_accounts()
    print('List of all customer accounts')
    print(all_accounts)




def delete_customer_account():
    '''
    Delete account by name
    '''
    customer_account_name = input('Enter customer name: ')
    account_exist = CustomerProfile.customer_exist(customer_account_name)
    if account_exist == True:
        find_account = CustomerProfile.search_customer_by_name(customer_name=customer_account_name)
        print('Are you sure you want to delete ' + str(find_account.customer_name) + '\'s account?')
        print('This account information will forever be lost!!!')
        print('''Enter 1 to delete account 
        or 
Enter 00 to exit''')
        danger = 0 
        while danger != "0":
            danger = input()
            if danger == "1":
                CustomerProfile.delete_customer(find_account)
                print("Account has been deleted!")
            elif danger == "00":
                delete_customer_account()
            break
    elif account_exist == False:
        print('Seems the account you searched for does not exist')






