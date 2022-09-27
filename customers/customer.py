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