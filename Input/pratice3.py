# Taking user inputs
item = input("What item do you wish to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many did you buy? "))

# Calculating total cost
cost = price * quantity

# Displaying the result
print(f"\nYou have bought {quantity} × {item} at ${price} each.")
print(f"Total cost is: ${round(cost, 2)}")

# Example Run:
# Input:
# What item do you wish to buy? Apple
# What is the price of the item? 1.5
# How many did you buy? 4
#
# Output:
# You have bought 4 × Apple at $1.5 each.
# Total cost is: $6.0
