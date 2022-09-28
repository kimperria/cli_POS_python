

def dashboard ():
    '''
    Menu function
    '''
    options = 0


    while options != "0":
        print("** User dashboard **")
        options = input(''' 
        1. Products
        2. Customers
        3. Purchases
        0. Close app
        
        From the list above select an option to continue: 
        ''')

        if options == "1":
            print("Products section")

        elif options == "2":
            print("Customer Section")
            select_task = input('''
            1. Create new customer account 
            2. Delete customer account 
            00. Back to dashboard ''')

            if select_task == "1":
                from customers import create_customer
                create_customer()
                print('Creating customer account...')
            elif select_task == "2":
                print('W.I.P')
            elif select_task == "00":
                print('Taking you back to the dashboard')
                dashboard()


        
        elif options == "0":
            print("Application is closing")
            print("Thank you. See you soon!")