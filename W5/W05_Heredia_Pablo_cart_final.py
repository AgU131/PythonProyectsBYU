# Programm Shopping Cart
# ¡showing creativity! #1. I controling typing error by using "str" instead of "int" for the Menu, but not yet over prices and quantities.
#2. It is allowed to register the quantity each item, and the total price include item's Sub Total. I also tabulated the properities each item.  


cart = []
item = ''
quantities = []
quantity = 0
prices = []
price = 0
option = '' 

print('\nWelcome to the Shopping Cart Program!')

# the menu option is in str type for avoiding input error
while option != "5":
    print ('\nPlease select one of the following: ')
    print (' 1. Add item \n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit')
    option = input('Please enter an action: ')
    
    if option == "1": # 1. Add item
        item = input('What item would you like to add? ')
        cart.append(item)
        price = float(input(f"What is the price of '{item.capitalize()}'? "))
        prices.append(price)
        quantity = int(input(f"How many of '{item.capitalize()}'? "))
        quantities.append(quantity)
        print(f"'{item.capitalize()}' has been added to the cart.")

    elif option == "2": #2. View cart
        print('\nThe contents of the shopping cart are: \n')

        print("#\tItem\tPrice\t Quantity")
        for i in range(len(cart)):
            print(f"{i+1}.\t{cart[i].capitalize()} \t${prices[i]:.2f} \t  {quantities[i]}")

    elif option == "3": # 3. Remove item
        
        print("\n#\tItem\tPrice\t Quantity")
        
        for i in range(len(cart)):
            print(f"{i+1}.\t{cart[i].capitalize()} \t${prices[i]:.2f} \t  {quantities[i]}")
        
        item = int(input('Which item would you like to remove? ') )
        if item > 0 and item <= len(cart):
            item -= 1
            cart.pop(item)
            prices.pop(item)
            quantities.pop(item)
            print(f'Item {item + 1} removed.')
        else :
            print(' please type the correct item number!! ')

        if len(cart) == 0 : print(' The cart is empty!! ')

    elif option == "4": # 4. Compute total

        print("\n#\tItem\tPrice\t Quantity")

        total = 0
        for i in range(len(cart)):
            subtotal = prices[i] * quantities[i]
            print(f"{i+1}.\t{cart[i].capitalize()} \t${prices[i]:.2f} \t  {quantities[i]} \t sub total: ${subtotal:.2f}")
            total += subtotal

        #for price in prices:
        #    total += price

        print(f'The total price of the items in the shopping cart is $ {total:.2f}')
            
    elif option == "5" : # 5. Quit
        print('\nThank you. Goodbye.!! ')

    else :# incorrect entry option : 
        print(' please type the correct option number!! ')