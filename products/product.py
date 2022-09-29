class ProductProfile:
    '''
    Class that helps to generate instances for creating a new product in this application
    '''
    # initialize list of product as empty as the class variable
    products_list = []

    def __init__(self, product_name, quantity, price, description):
        '''
        Method that defines properties of this class.

        Args: 
            product's name
            other arguements
        '''
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.description = description

    def __repr__(self):
        '''
        Method to display product  with their name
        '''
        return '<ProductProfile {}>'.format(self.product_name)

    def save_product(self):
        '''
        Method to create and save new product infomation
        '''
        ProductProfile.products_list.append(self)

    def delete_product(self):
        '''
        Method to remove product instance
        '''
        ProductProfile.products_list.remove(self)

    @classmethod
    def search_product_by_name(cls, product_name):
        '''
        Method to find product by name

        Args: 
            Product name
        Return:
            Product found in list
        '''
        #loop the contact list
        for product in cls.products_list:
            if product.product_name == product_name:
                return product

    @classmethod
    def product_exist(cls, product_name):
        '''
        Method to check product by name
        '''
        for product in cls.products_list:
            if product.product_name == product_name:
                return True
        return False

    @classmethod
    def display_products(cls):
        '''
        Show all product accounts
        '''
        return cls.products_list
                
