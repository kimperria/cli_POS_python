from .product import ProductProfile
import json
products_database = 'database/products.json'

def create_product_id():

    with open(products_database, 'r') as db:
        items = json.load(db)
        print(items)
        if not items:
            id = 0
            id += 1
            product_id = 'P000' + str(id)
            return product_id
        

def create_product():
    '''
    Create new product
    '''
    print('********************')
    print('Enter requested details to create new product into the system')
    product_id = create_product_id()
    print(product_id)
    product_name = input('''Enter name of the new product: ''')
    quantity = input('''Enter quantity received: ''')
    price = input('''Enter price: ''')
    description = input('''Tell about the product: ''')

    print('Creating product...')

    product_info = {}
    product_info = ProductProfile(product_name = product_name, quantity=quantity, price=price, description=description)
    print('Please wait!! Saving to database...')
    # CustomerProfile.save_product(product_info)
    product = {}
    # Serialize class instance to JSON
    product[product_id] = json.dumps(product_info.__dict__)
    with open(products_database, 'r+') as db:
        items = json.load(db)
        if not items:
            json.dump(product, db)
    print("New product: " + product_info.product_name + " has been created successfully.")


    return product_info




def display_all_products():
    '''
    Show all products
    '''
    all_products = ProductProfile.display_products()
    print('List of all products')
    print(all_products)




def delete_product():
    product_name = input('Enter product name: ')
    product_exist = ProductProfile.product_exist(product_name)
    if product_exist == True:
        find_account = ProductProfile.search_product_by_name(product_name=product_name)
        print('Are you sure you want to delete ' + str(find_account.product_name))
        print('This information will forever be lost!!!')
        print('''Enter 1 to confirm delete 
        or 
Enter 00 to exit''')
        danger = 0 
        while danger != "0":
            danger = input()
            if danger == "1":
                ProductProfile.delete_product(find_account)
                print("Product has been deleted!")
            elif danger == "00":
                delete_product()
            break
    elif product_exist == False:
        print('Seems the account you searched for does not exist')






