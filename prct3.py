import math

# Taking input for sides A and B
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

# Calculating the hypotenuse using the Pythagorean theorem
c = math.sqrt(a**2 + b**2)

# Displaying the result rounded to 2 decimal places
print(f"Side C = {round(c, 2)}")
