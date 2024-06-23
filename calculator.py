operator = input("Enter the operator to perform the operation(+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
def add(num1,num2):
    return num1 + num2
result1 = add(num1,num2)
def subtract(num1,num2):
    return num1 - num2
result2 = subtract(num1,num2)
def multiply(num1,num2):
    return num1*num2
result3 = multiply(num1,num2)
def divide(num1,num2):
    return num1/num2
result4 = divide(num1,num2)

if operator == "+":
    print(round(result1,3))
elif operator == "-":
    print(round(result2,3))
elif operator == "*":
    print(round(result3,3))
elif operator == "/":
    print(round(result4,3))
else:
    print("Invalid operator !")