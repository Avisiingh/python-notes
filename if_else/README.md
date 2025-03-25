# Conditional Statements in Python

This script demonstrates the use of conditional statements (`if-elif-else`) in Python.  
It takes user input for age, food preference, and name, then prints appropriate messages based on the given conditions.

## **Code Explanation**

```python
# Prompt user to enter their age
age = int(input("Enter your age: "))  

# Check different conditions based on the age entered
if age >= 100:
    print("Namastey dada ji! You don't need to sign up. Please be safe and take rest, this is not for you.")  
    # Example input: 105  
    # Output: Namastey dada ji! You don't need to sign up. Please be safe and take rest, this is not for you.
elif age >= 18:
    print("You are now signed up!")  
    # Example input: 25  
    # Output: You are now signed up!
elif age < 0:
    print("You have not been born yet.")  
    # Example input: -5  
    # Output: You have not been born yet.
else:
    print("You must be 18+ to sign up.")  
    # Example input: 10  
    # Output: You must be 18+ to sign up.

# Asking user for a response about food
response = input("Do you want some food? (y/n): ")  

if response.lower() == "y":  # Converts input to lowercase for better handling
    print("Here, have some food!")  
    # Example input: y  
    # Output: Here, have some food!
else:
    print("No food for you!")  
    # Example input: n  
    # Output: No food for you!

# Prompt user to enter their name
name = input("Enter your name: ")  

if name.strip() == "":  # Using strip() to remove accidental spaces
    print("You did not type your name!")  
    # Example input: (empty)  
    # Output: You did not type your name!
else:
    print(f"Hello, {name}!")  
    # Example input: Alice  
    # Output: Hello, Alice!

# Check if an item is for sale
for_sale = True  # Boolean variable

if for_sale:
    print("This item is for sale.")  
    # Output: This item is for sale.
else:
    print("This item is NOT for sale.")  
    # (This branch will never run since for_sale is always True)


