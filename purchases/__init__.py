from customers import CustomerProfile
from products import ProductProfile
from purchases import *
import json


def purchase_items():
    '''
    Validate user to be exisiting customer
    '''
    customer_id = input('Enter your customer ID before purchase: ')
    if CustomerProfile.customer_exist_by_id(customer_id=customer_id):
        customer = CustomerProfile.search_customer_by_id(customer_id).get('customer_name')
        print('***********')
        print(f"Welcome {customer}")
        while True:
            print('***********')
            print('What would you like to buy? ')
            product_id = input('Enter product ID: ')
            product_requested = ProductProfile.product_exist_by_id(product_id)
            if product_requested == True:
                product_name = ProductProfile.search_product_by_id(product_id).get('product_name')
                product_price = ProductProfile.search_product_by_id(product_id).get('price')
                product_quantity = ProductProfile.search_product_by_id(product_id).get('quantity')
                product_description = ProductProfile.search_product_by_id(product_id).get('description')
                try :
                    print(f'Available in store: {product_quantity}')
                    quantity_requested = int(input(f'Enter quantity of {product_name} you want? '))

                    if quantity_requested <= product_quantity:
                        '''
                        Validate quantity
                        '''
                        product_total = product_price * quantity_requested
                        print(f'Product Total {product_total}')

                        purchases_database = 'database/purchases.json'
                        with open(purchases_database, 'r') as purchase_records:
                            purchases = json.load(purchase_records)
                            if purchases == []:
                                id = 1
                                purchase_id = 'S000' + str(id)
                                purchase = {
                                    'purchase_id': purchase_id,
                                    'customer_id': customer_id,
                                    'product': product_name,
                                    'quantity': quantity_requested,
                                    'total_price': product_total
                                }
                            elif purchases != []:
                                id = 1
                                for purchase in purchases:
                                    id = id + 1
                                    purchase_id = 'S000' + str(id)
                                    purchase = {
                                    'purchase_id': purchase_id,
                                    'customer_id': customer_id,
                                    'product': product_name,
                                    'quantity': quantity_requested,
                                    'total_price': product_total
                                    }
                            purchases.append(purchase)
                            print('**************')
                            print('Please wait!! Saving to database')
                            with open(purchases_database, 'w') as purchase_records:
                                json.dump(purchases, purchase_records, indent=4)


                            '''
                            Reduce quantity in store
                            '''
                            quantity_in_store = ProductProfile.search_product_by_id(product_id).get('quantity')
                            remaining_quantity = quantity_in_store - quantity_requested
                            # print('leftover', remaining_quantity)
                            
                            ProductProfile.update_product(product_id=product_id, product_name=product_name, quantity=remaining_quantity, price=product_price, description=product_description)


                    elif quantity_requested > product_quantity:
                        print('Warning')
                        print("!!!!!!!!!!")
                        print('Amount asked is more than quantity available in stock.')
                    else:
                        return product_quantity
                except ValueError:
                    print('Quantity must be interger')
            elif product_requested == False:
                print('Warning !!!!')
                print('Please enter valid ID')




            # check_out = input('''Enter:
            # 1. To continue shopping
            # 2. To proceed to checkout ''')
            # if check_out == "1":
            #     '''
            #     Make new sale
            #     '''

            # elif check_out == "2":
            #     '''
            #     Checkout
            #     '''
            # else:
            #     print('Warning!: Invalid input')
            #     print('Please check choices provided then try again.')


    else:
        print("Check your ID to be correct or create customer account in customers menu.")