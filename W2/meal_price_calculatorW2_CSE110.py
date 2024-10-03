# Project 02: Meal Price Calculator 
    # Created by Agustin Heredia

# I added a short welcome to the program
print('Hi customer!\nPlease enter the following: \n')
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

# Here i added a section of drinks you can add to your meal price
drinks = float(input("What is the price of a drink? "))
number_of_drinks = int(input("How many drinks did you buy? "))
print()

food_price = child_meal * children + adult_meal * adults + drinks * number_of_drinks
print(f"Subtotal: ${str(food_price)}")
print()

tax_rate = float(input("What is the sales tax rate? "))
aplly_tax = food_price * (tax_rate / 100)
print(f"Sales Tax: ${str(aplly_tax)}")

# Here i created a variable with the culmination of the price (total and final price), by ading the food price plus food taxes
total_price = aplly_tax + food_price
print(f"Total: ${total_price}")
print()

payment_amount = float(input("What is the payment amount? "))
print(f"Change: ${str(payment_amount - total_price)}")

# I also added a last nice line
print("I hope you enjoyed the food!")