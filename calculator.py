# Simple Calculator
num1 = float(input("Enter the first number: "))
operation = input("Choose an operation (add, sub, div, mult): ")
num2 = float(input("Enter the second number: "))

if operation == "add":
    print(num1 + num2)

elif operation == "sub":
    print(num1 - num2)

elif operation == "mult":
    print(num1 * num2)

elif operation == "div":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operation. Please choose: add, sub, div, or mult.")