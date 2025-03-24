# User Input and Data Processing in Python

## Getting User Input
```python
name = input("Enter your name: ")
```
**Example Input:**
```
Enter your name: Avinash
```
**Output:**
```
Hello Avinash
```

## Handling Integer Input
```python
age = int(input("Enter your age: "))  # Convert input to an integer
age += 1  # Increment age by 1
```
**Example Input:**
```
Enter your age: 25
```
**Output:**
```
You are 26 years old.
```

## Fun Word Game
```python
adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
verb = input("Enter a verb: ")
```
**Example Input:**
```
Enter an adjective: amazing
Enter a noun: lion
Enter another adjective: ferocious
Enter one more adjective: excited
Enter a verb: roaring
```
**Output:**
```
Today I went to an amazing zoo.
In an exhibit, I saw a lion.
The lion was ferocious and roaring.
I was excited!
```

## Calculating the Area of a Rectangle
```python
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area is: {area} m²")
```
**Example Input:**
```
Enter the length of the rectangle: 5
Enter the width of the rectangle: 10
```
**Output:**
```
The area is: 50 m²
```

## Shopping Cart Calculation
```python
item = input("What item do you wish to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many did you buy? "))
```
**Example Input:**
```
What item do you wish to buy? Apples
What is the price of the item? 2.5
How many did you buy? 4
```
**Output:**
```
You have bought 4 x Apples at $2.5 each.
Total cost is: $10.0
```



