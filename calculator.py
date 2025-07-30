# Simple Calculator
num1 = int (input ("enter a number: "))
operation = input ("choose : add, sub, div, mult: ")
num2 = int (input ("enter another number: "))
if operation == "add" :
    print (num1 + num2)
elif operation == "sub" :
    print (num1 - num2)
elif operation == "div" :
    print (num1 / num2) 
elif operation == "mult" :
    print (num1 * num2)
else :
    print ("invalid input. Please enter a number!")