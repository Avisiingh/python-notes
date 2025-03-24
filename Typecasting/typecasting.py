# Typecasting in Python

# Typecasting is the process of converting a value from one data type to another. 
# It can be done explicitly (manually) or implicitly (automatically by Python).

# Defining variables of different data types
name = "avinash"  # String
age = 21          # Integer
gpa = 2.5         # Float
student = True    # Boolean

# Checking the data types of the variables
print(type(name))    # Output: <class 'str'>
print(type(age))     # Output: <class 'int'>
print(type(gpa))     # Output: <class 'float'>
print(type(student)) # Output: <class 'bool'>

# Explicit Conversion (Manual Typecasting)

# Converting 'age' (integer) to float
age = float(age)
print(age)           # Output: 21.0
print(type(age))     # Output: <class 'float'>

# Converting 'gpa' (float) to integer (removes decimal part)
gpa = int(gpa)
print(gpa)          # Output: 2

# Converting 'student' (boolean) to string
student = str(student)
print(student)      # Output: "True"
print(type(student)) # Output: <class 'str'>

# Converting 'age' (float) to boolean
age = bool(age)
print(age)          # Output: True (since age was 21.0, any nonzero number is True)

# Setting 'age' to 0 and converting to boolean
age = 0
age = bool(age)
print(type(age))    # Output: <class 'bool'>
print(age)          # Output: False (0 is treated as False in boolean conversion)

# Implicit Conversion (Automatic Typecasting by Python)

x = 2   # Integer
y = 2.0 # Float

# Performing division, Python automatically converts the result to float
x = x / y  
print(x)           # Output: 1.0 (integer 2 is implicitly converted to float)
print(type(x))     # Output: <class 'float'>
