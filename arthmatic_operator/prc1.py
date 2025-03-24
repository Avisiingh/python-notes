import math

# Taking radius as input
radius = float(input("Enter the radius of the circle: "))

# Calculating circumference
circumference = 2 * math.pi * radius

# Displaying the result rounded to 2 decimal places
print(f"The circumference is: {round(circumference, 2)}")
