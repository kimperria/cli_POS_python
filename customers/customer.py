import json


class CustomerProfile:
    '''
    Class that helps to generate instances for creating a new customer account on this application
    '''
    # initialize list of customers as empty as the class variable
    # customers_list = []

    def __init__(self, customer_id, customer_name, location, contact):
        '''
        Method that defines properties of this class.

        Args: 
            customer's name
            Their location and contact
        '''
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.location = location
        self.contact = contact

    def __repr__(self):
        '''
        Method to display customer profile with their name
        '''
        return f'name:{self.customer_name}, location:{self.location}, contact:{self.contact}'

    @classmethod
    def save_customer(cls, customer_name, location, contact):
        '''
        Method to create and save new customer infomation
        '''
        customers_database = 'database/customers.json'
        with open(customers_database, 'r') as customers_file:
            customer_accounts = json.load(customers_file)
            try:
                if customer_accounts == []:
                    print("There are no customer accounts in database")
                    id = 1
                    customer_id = 'C000' + str(id)
                elif customer_accounts !=[]:
                    id = 1
                    for customer in customer_accounts:
                        id = id + 1
                        customer_id = 'C000' + str(id)
                        customer = {
                            "customer_id": customer_id,
                            "customer_name":customer_name,
                            "location": location,
                            "contact":contact
                        }
                customer_accounts.append(customer)
                print('Please wait!! Saving to database...')
                with open(customers_database, "w") as customer_file:
                    json.dump(customer_accounts, customer_file, indent=4)
                    print("Customer Account Created Successfully")
            except:
                print("Unable to create customer account")

    def delete_customer(self):
        '''
        Method to remove customer instance
        '''
        CustomerProfile.customers_list.remove(self)

    @classmethod
    def search_customer_by_name(cls, customer_name):
        '''
        Method to find customer by name

        Args: 
            customer name
        Return:
            Customer found in list
        '''
        #loop the contact list
        for customer in cls.customers_list:
            if customer.customer_name == customer_name:
                return customer

    @classmethod
    def customer_exist(cls, customer_name):
        '''
        Method to check customer account by name
        '''
        for customer in cls.customers_list:
            if customer.customer_name == customer_name:
                return True
        return False

    @classmethod
    def display_customer_accounts(cls):
        '''
        Show all customer accounts
        '''
        return cls.customers_list
                
