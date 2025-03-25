
# Conditional Statements in Python - Notes
## **1. Age-Based Conditions**


```python
age = int(input("Enter your age: "))  # Takes user input and converts it to an integer.

if age >= 100:
    print("Namastey dada ji! You don't need to sign up. Please be safe and take rest, this is not for you.")  
elif age >= 18:
    print("You are now signed up!")  
elif age < 0:
    print("You have not been born yet.")  
else:
    print("You must be 18+ to sign up.")  
```
**Explanation:**
- If `age >= 100`: Prints a message that the person does not need to sign up.
- If `age >= 18`: Signs the user up.
- If `age < 0`: Indicates an invalid age.
- Else: The user is too young to sign up.

---

## **2. Food Preference Condition**
This code asks the user if they want food and prints a response accordingly.

```python
response = input("Do you want some food? (y/n): ")  # Takes user input.

if response.lower() == "y":  # Converts input to lowercase to avoid case mismatches.
    print("Here, have some food!")  
else:
    print("No food for you!")  
```
**Explanation:**
- If the user inputs `"y"` (case insensitive), it prints **"Here, have some food!"**
- Otherwise, it prints **"No food for you!"**

---

## **3. Name Input Handling**
This code handles cases where a user may not enter a name.

```python
name = input("Enter your name: ")  # Takes user input.

if name.strip() == "":  # The strip() function removes spaces to avoid blank input.
    print("You did not type your name!")  
else:
    print(f"Hello, {name}!")  
```
**Explanation:**
- If the user leaves the name blank, it prints **"You did not type your name!"**
- Otherwise, it greets the user by name.

---

## **4. Item Availability Condition**
This code checks whether an item is available for sale.

```python
for_sale = True  # Boolean variable indicating if the item is for sale.

if for_sale:
    print("This item is for sale.")  
else:
    print("This item is NOT for sale.")  
```
**Explanation:**
- If `for_sale` is `True`, it prints **"This item is for sale."**
- Otherwise, it prints **"This item is NOT for sale."**

---

## **Summary**
- **`if-elif-else` statements** allow checking multiple conditions.
- **Boolean conditions (`True` or `False`)** help in decision-making.
- **Input handling (`input()`, `strip()`, `lower()`)** ensures smooth user interaction.

---
# Simple Calculator in Python

---

## **Code Explanation**

```python
# Taking operator input from the user
operator = input("Enter your operator (+ - * /): ")

# Taking two numerical inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing operations based on the operator entered
if operator == "+":
    result = num1 + num2
    print(round(result, 3))  # Rounds result to 3 decimal places

elif operator == "-":
    result = num1 - num2
    print(round(result, 3))

elif operator == "*":
    result = num1 * num2
    print(round(result, 3))

elif operator == "/":
    result = num1 / num2
    print(round(result, 3))

else:
    print(f"{operator} is not a valid operator.")
