def dashboard ():
    '''
    Menu function
    '''
    options = 0
    print(type(options))


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
            print(type(options))

        
        elif options == "0":
            print("Application is closing")
            print("Thank you. See you soon!")
            print(type(options))