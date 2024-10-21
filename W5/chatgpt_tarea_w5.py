# First prepare the list, just like the previous checkpoint
print("Please enter the items of the shopping list (type: quit to finish):")

shopping_list = []
item = None

while item != "quit":
    item = input("Item: ")

    if item != "quit":
        shopping_list.append(item)

# We now have the list. Print it out to verify:
print("\nThe shopping list is:")
for item in shopping_list:
    print(item)

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

    # I could have just put shopping_list[i] directly in my print statement
    # rather than creating a separate variable if I wanted. I decided to do it
    # this way to make it easier to read.

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shopping_list[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

"""
extra con creativity:

    # Shopping Cart Program with Creative Features
# Added feature: The program now tracks the quantity of items in the cart and includes input validation for item removal. 
# Prices are neatly aligned, and the total price includes quantity in the calculation. 

# Lists to store item names, prices, and quantities
cart_items = []
cart_prices = []
cart_quantities = []

def display_menu():
    # Displays the menu options to the user
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
def add_item():
    # Adds an item, its price, and quantity to the cart
    item = input("What item would you like to add? ")
    price = float(input(f"What is the price of '{item}'? "))
    quantity = int(input(f"How many '{item}' would you like to add? "))
    cart_items.append(item)
    cart_prices.append(price)
    cart_quantities.append(quantity)
    print(f"'{item}' has been added to the cart.")

def view_cart():
    # Displays the contents of the shopping cart
    if cart_items:
        print("\nThe contents of the shopping cart are:")
        for i in range(len(cart_items)):
            print(f"{i+1}. {cart_items[i]} - ${cart_prices[i]:.2f} x {cart_quantities[i]}")
    else:
        print("\nYour cart is empty.")

def remove_item():
    # Removes an item from the cart based on the user's input.
    if cart_items:
        view_cart()
        try:
            item_number = int(input("Which item would you like to remove? ")) - 1
            if 0 <= item_number < len(cart_items):
                removed_item = cart_items.pop(item_number)
                cart_prices.pop(item_number)
                cart_quantities.pop(item_number)
                print(f"{removed_item} has been removed from the cart.")
            else:
                print("Sorry, that is not a valid item number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Your cart is empty.")

def compute_total():
    # Computes and displays the total price of the items in the cart.
    total = 0
    for i in range(len(cart_prices)):
        total += cart_prices[i] * cart_quantities[i]
    print(f"\nThe total price of the items in the shopping cart is: ${total:.2f}")

# Main program loop
print("Welcome to the Shopping Cart Program!")
while True:
    display_menu()
    action = input("Please enter an action: ")
    
    if action == "1":
        add_item()
    elif action == "2":
        view_cart()
    elif action == "3":
        remove_item()
    elif action == "4":
        compute_total()
    elif action == "5":
        print("Thank you. Goodbye.")
        break
    else:
        print("Please select a valid option.")

#I added a description comment at the top to explain the extra feature. The program now tracks quantities, aligns prices, and performs input validation when removing items.
"""