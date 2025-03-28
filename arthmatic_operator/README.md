# Python Mathematical Operations Explained

## Rounding Numbers
```python
x = 3.14
result = round(x)
print(result)  # Output: 3
```
- `round(x)`: Rounds `x` to the nearest integer.

## Absolute Value
```python
y = -4
result = abs(y)
print(result)  # Output: 4
```
- `abs(y)`: Returns the absolute value of `y`.

## Exponentiation
```python
result = pow(4, 3)
print(result)  # Output: 64
```
- `pow(a, b)`: Computes `a` raised to the power `b` (4^3 = 64).

## Finding Maximum and Minimum
```python
x = 3.14
y = -4
z = 5
result = max(x, y, z)
print(result)  # Output: 5
```
- `max(x, y, z)`: Returns the largest value among the given numbers.

```python
result = min(x, y, z)
print(result)  # Output: -4
```
- `min(x, y, z)`: Returns the smallest value.

## Using Augmented Assignment Operators
```python
friends = 5
friends += 1  # friends = friends + 1
friends -= 2  # friends = friends - 2
friends *= 3  # friends = friends * 3
friends /= 2  # friends = friends / 2
friends **= 2  # friends = friends squared
reminder = friends % 5  # Modulus operation
print(reminder)
```
- These operators simplify mathematical operations.

## Using the `math` Module
```python
import math
print(math.pi)  # Output: 3.141592653589793
```
- `math.pi`: Returns the value of Pi.

### Calculating the Circumference of a Circle
```python
import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}")
```
- Uses `math.pi` to calculate the circumference: `2 * π * r`.

### Calculating the Area of a Circle
```python
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
print(f"The area of the circle is: {round(area, 2)} m^2")
```
- Uses `math.pi` to compute the area: `π * r^2`.

### Special Constants
```python
print(math.e)  # Output: 2.718281828459045
```
- `math.e`: Euler's number, useful in logarithmic and exponential calculations.

### Using `math.sqrt()` and `math.ceil()`
```python
x = 9
result = math.sqrt(x)
print(result)  # Output: 3.0
```
- `math.sqrt(x)`: Computes the square root of `x`.

```python
result = math.ceil(4.2)
print(result)  # Output: 5
```
- `math.ceil(x)`: Rounds `x` up to the nearest integer.

```python
result = math.floor(4.9)
print(result)  # Output: 4
```
- `math.floor(x)`: Rounds `x` down to the nearest integer.

### Calculating Hypotenuse Using Pythagorean Theorem
```python
import math
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}")
```
- Uses the Pythagorean Theorem: `c = sqrt(a^2 + b^2)`.


