import json


class ProductProfile:
    '''
    Class that helps to generate instances for creating a new product in this application
    '''

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

    @classmethod
    def display_all_products(cls):
        '''
        Show all product accounts
        '''
        product_database = 'database/products.json'
        with open(product_database, 'r') as products_file:
            products = json.load(products_file)
            for product in products:
                id = product["product_id"]
                product_name = product['product_name']
                product_quantity = product['quantity']
                product_price = product['price']
                product_description = product['description']
                print(f'Product ID : {id}')
                print(f'Product Name : {product_name}')
                print(f'Quantity in store : {product_quantity}')
                print(f'Price : {product_price}')
                print(f'Description : {product_price}')
                print('\n\n')

    @classmethod
    def product_exist(cls, product_name):
        '''
        Method to check product by name
        '''
        product_database = 'database/products.json'
        file = open(product_database, 'r')
        products = json.load(file)
        isPresent = False
        for product in products:
            if product.get("product_name") == product_name:
                isPresent = True
        return isPresent

    @classmethod
    def search_product_by_name(cls, product_name):
        '''
        Method to find product by name

        Args: 
            Product name
        Return:
            Product found in list
        '''
        product_database = 'database/products.json'
        with open(product_database, 'r') as products_file:
            products = json.load(products_file)
            for product in products:
                try: 
                    if product.get("product_name") == product_name:
                        print('*************')
                        print('Item found')
                        print(product)
                        print('*************')
                except:
                    print("Product not in system.")

    @classmethod
    def search_product_by_id(cls, product_id):
        '''
        Method to search product bt ID
        '''
        product_database = 'database/products.json'
        file =  open(product_database, 'r')
        products = json.load(file)
        product = ""
        for product in products:
            if product.get("product_id") == product_id:
                product = product
        return product

    @classmethod
    def product_exist_by_id(cls, product_id):
        '''
        Validation method by ID
        '''
        product_database = 'database/products.json'
        file = open(product_database, 'r')
        products = json.load(file)
        isPresent = False
        for product in products:
            if product.get("product_id") == product_id:
                isPresent = True
        return isPresent

    @classmethod
    def update_product(self, product_id, product_name, quantity, price, description):
        product_database = 'database/products.json'
        file = open(product_database, 'r')
        products = json.load(file)

        for product in products:
            if product.get("product_id") == product_id:
                product.update({
                    "product_id": product_id,
                    "product_name": product_name,
                    "quantity": quantity,
                    "price": price,
                    "description": description
                })
                print('Saving changes ...')
        with open(product_database, 'w') as products_file:
            json.dump(products, products_file, indent=4)



    @classmethod        
    def delete_product(cls, product_id):
        '''
        Method to remove product instance
        '''
        product_database = 'database/products.json'
        file = open(product_database, 'r')
        products = json.load(file)
        for product in products:
            if product.get("product_id") == product_id:
                products.remove(product)
                id = product["product_id"]
                name = product["product_name"]
                print(f"Product ID: {id}")
                print(f"Product Name: {name}")
                print('\n\n')
                with open(product_database, 'w') as products_file:
                    json.dump(products, products_file, indent=4)