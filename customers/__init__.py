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






