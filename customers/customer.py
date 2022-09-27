class CustomerProfile:
    '''
    Class that helps to generate instances for creating a new customer account on this application
    '''
    # initialize list of customers as empty as the class variable
    customers_list = []

    def __init__(self, customer_name, location, contact):
        '''
        Method that defines properties of this class.

        Args: 
            customer's name
            Their location and contact
        '''
        self.customer_name = customer_name
        self.location = location
        self.contact = contact

    def __repr__(self):
        '''
        Method to display customer profile with their name
        '''
        return '<CustomerProfile {}>'.format(self.customer_name)

    def save_customer(self):
        '''
        Method to create and save new customer infomation
        '''
        CustomerProfile.customers_list.append(self)

    def delete_customer(self):
        '''
        Method to remove customer instance
        '''
        CustomerProfile.customers_list.remove(self)