operator =input("enter your operator (+ - *): ")
num1= float(input("enter the first number: "))
num2= float(input("enter the second number: "))

if operator == "+":
    result =num1 + num2

    print(round(result,3))
elif operator == "-":
    result =num1 - num2
    print(round(result,3))
elif operator == "*":
    result =num1 * num2
    print(round(result,3))
elif operator=="/":
    result =num1 / num2
    print(round(result,3))
else:
    print(F"{operator} is not valid.")