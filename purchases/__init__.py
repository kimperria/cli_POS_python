from customers import CustomerProfile
from products import ProductProfile
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
        receipts = []
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

                            receipt = {
                                "product_name": product_name,
                                "quantity": quantity_requested,
                                "Total": product_total
                            }
                            receipts.append(receipt)
                            print(receipts)
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

                            shop_again = ''
                            while True:
                                print('''Enter:
                        1. To continue shopping 
                        2. Proceed to checkout ''')
                                check_out = input('Enter your choice...')

                                if check_out != '':
                                    if check_out == '1':
                                        shop_again = check_out
                                        break
                                    elif check_out == '2':
                                        shop_again = '2'
                                        break
                                    else:
                                        print('Warning!: Invalid input')
                                        print('Please check choices provided then try again.')
                                        continue
                                else:
                                    print('Please choose one option')
                                    print('Please choose one option. Please check choices provided then try again.')
                                    continue
                            
                            if shop_again == '1':
                                continue
                            elif shop_again == '2':
                                print('Thank you for shopping with us! Below is your receipt.')
                                print("\n------------------------------------")
                                print('-------------BINGU POS-----------------')
                                print('--------OFFICIAL SALES RECEIPT---------')
                                print('************************************')
                                print("Customer name: ", customer)
                                print("Purchase || Quantity || Total")
                                print(receipts)
                                grand_total = []
                                for i in receipts:
                                    grand_total.append(i.get('Total'))
                                print(f"Total Amount = {str(sum(grand_total))}")
                                print("\n------------------------------------")
                                print('Goods once sold cannot be returned')
                                print('************************************')
                                print('Program developed by kimperria')
                                print('************************************')

                                receipts_database = 'database/receipt.json'
                                history = {}
                                with open(receipts_database, 'r') as receipts_file:
                                    data = json.load(receipts_file)
                                    if data == []:
                                        id = 1
                                        receipt_id = 'R000' + str(id)
                                        history[customer_id] = receipts
                                    elif data != []:
                                        id = 1
                                        for item in data:
                                            id = id + 1
                                            receipt_id = 'R000' + str(id)
                                            history[customer_id] = receipts
                                    data.append(history)
                                    with open(receipts_database, 'w') as receipts_file:
                                        json.dump(data, receipts_file, indent=4)
                            break
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

    else:
        print("Check your ID to be correct or create customer account in customers menu.")