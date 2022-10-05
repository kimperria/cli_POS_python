import json


class ProductProfile:
    '''
    Class that helps to generate instances for creating a new product in this application
    '''
    # initialize list of product as empty as the class variable
    products_list = []

    def __init__(self, product_id ,product_name, quantity, price, description):
        '''
        Method that defines properties of this class.

        Args: 
            product's name
            other arguements
        '''
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.description = description

    def __repr__(self):
        '''
        Method to display product  with their name
        '''
        return '<ProductProfile {}>'.format(self.product_name)

    @classmethod
    def save_product(cls, product_name, quantity, price, description):
        '''
        Method to create and save new product infomation
        '''
        product_database = 'database/products.json'
        with open(product_database, 'r') as products_file:
            products = json.load(products_file)
            print(products)
            try:
                if products == []:
                    id = 1
                    product_id = 'P000' + str(id)
                    product = {
                        "product_id":product_id,
                        "product_name": product_name,
                        "quantity": quantity,
                        "price": price,
                        "description": description
                    }
                elif products != []:
                    id = 1
                    for product in products:
                        id = id + 1
                        product_id = 'P000' + str(id)
                        product = {
                        "product_id":product_id,
                        "product_name": product_name,
                        "quantity": quantity,
                        "price": price,
                        "description": description
                        }
                products.append(product)
                print("Please wait!! Saving to database")
                with open(product_database, 'w') as products_file:
                    json.dump(products, products_file, indent=4)
            except:
                print('Unable to create product')

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
                
