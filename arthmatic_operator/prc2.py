import math

# Taking radius as input
radius = float(input("Enter the radius of a circle: "))

# Calculating area
area = math.pi * radius * radius  # or area = math.pi * (radius ** 2)

# Displaying the result rounded to 2 decimal places
print(f"The area of the circle is: {round(area, 2)} m²")
