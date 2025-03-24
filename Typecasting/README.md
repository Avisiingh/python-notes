# Typecasting in Python

Typecasting is the process of converting a value from one data type to another.
It can be done explicitly (manually) or implicitly (automatically by Python).

## Defining Variables
```python
name = "avinash"  # String
age = 21          # Integer
gpa = 2.5         # Float
student = True    # Boolean
```

## Checking Data Types
```python
print(type(name))    # Output: <class 'str'>
print(type(age))     # Output: <class 'int'>
print(type(gpa))     # Output: <class 'float'>
print(type(student)) # Output: <class 'bool'>
```

## Explicit Conversion (Manual Typecasting)

### Converting Integer to Float
```python
age = float(age)
print(age)           # Output: 21.0
print(type(age))     # Output: <class 'float'>
```

### Converting Float to Integer
```python
gpa = int(gpa)
print(gpa)          # Output: 2
```

### Converting Boolean to String
```python
student = str(student)
print(student)      # Output: "True"
print(type(student)) # Output: <class 'str'>
```

### Converting Float to Boolean
```python
age = bool(age)
print(age)          # Output: True (any nonzero number is True)
```

### Converting Zero to Boolean
```python
age = 0
age = bool(age)
print(type(age))    # Output: <class 'bool'>
print(age)          # Output: False (0 is treated as False)
```

## Implicit Conversion (Automatic Typecasting by Python)
```python
x = 2   # Integer
y = 2.0 # Float

# Performing division, Python automatically converts the result to float
x = x / y  
print(x)           # Output: 1.0
print(type(x))     # Output: <class 'float'>
```

### Summary
- **Explicit Conversion**: Done manually using `int()`, `float()`, `str()`, `bool()`.
- **Implicit Conversion**: Done automatically by Python where needed.
- **Boolean Rules**: `0` is `False`, any nonzero value is `True`.



