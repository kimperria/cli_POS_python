from .product import ProductProfile
products_database = 'database/products.json'       

def create_product():
    '''
    Create new product
    '''
    print('********************')
    print('Enter requested details to create new product into the system')
    product_name = input('''Enter name of the new product: ''')
    quantity = int(input('''Enter quantity received: '''))
    price = float(input('''Enter price: '''))
    description = input('''Tell about the product: ''')
    try: 
        print('Creating product...')
        ProductProfile.save_product(product_name, quantity, price, description)
    except:
        print("Something went wrong")




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






