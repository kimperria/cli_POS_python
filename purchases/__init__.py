from customers import CustomerProfile
from products import ProductProfile
import os
import json

def purchase_items():
    '''
    Validate user to be exisiting customer
    '''
    customer_id = input('Enter your customer ID before purchase: ')
    if CustomerProfile.customer_exist_by_id(customer_id=customer_id):
        print("Proceed")
        while True:
            print('Create order')
            print('***********')
            product_id = input('Enter product ID: ')
            product_ordered = ProductProfile.search_product_by_id(product_id)
            # print(product_ordered)
            product_name = ProductProfile.search_product_by_id(product_id).get('product_name')
            price = ProductProfile.search_product_by_id(product_id).get('price')
            try:
                quantity = int(input(f'Enter quantity of {product_name} you want? '))
            except ValueError:
                print('Quantity must be interger')
                continue
            product_quantity = product_ordered.get('quantity')
            if quantity <= product_quantity:
                '''
                Calculating invoice amount
                '''
                order_total = price * quantity
                print('Total price is: ', order_total)
                '''
                Save transaction to database
                '''
                purchases_database = 'database/purchases.json'
                with open(purchases_database, 'r') as purchase_records:
                    purchases = json.load(purchase_records)
                    try: 
                        if purchases == []:
                            id = 1
                            purchase_id = 'S000' + str(id)
                            purchase = {
                                    'purchase_id': purchase_id,
                                    'bought_by': customer_id,
                                    'product_name':product_name,
                                    'quantity': quantity,
                                    'price': order_total
                                }
                        elif purchases != []:
                            id = 1
                            for purchase in purchases:
                                id = id + 1
                                purchase_id = 'S000' + str(id)
                                purchase = {
                                    'purchase_id': purchase_id,
                                    'bought_by': customer_id,
                                    'product_name':product_name,
                                    'quantity': quantity,
                                    'price': order_total,
                                }
                        purchases.append(purchase)
                        print('**************')
                        print('Please wait!! Saving to database')
                        print(purchases)
                        with open(purchases_database, 'w') as purchase_records:
                            json.dump(purchases, purchase_records, indent=4)
                    except ValueError:
                        print("Unable to save order. Please contact admin.")
                        break
            elif quantity > product_quantity:
                print("!!!!!!!!!!")
                print('Amount asked is more than quantity available in stock.')
            else:
                return quantity

    else:
        print("Check your ID to be correct or create customer account in customers menu.")