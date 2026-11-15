# Simple Calculator

#input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter last number: "))
op = input("Enter operator (+, -, *, /): ")

#condition
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/': 
    if num2 == 0: print("Cannot divide by zero")
else: print(num1 / num2)

#code completed :)