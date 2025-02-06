# This is my cacalator function script

def add(num1,num2):
    result = num1 + num2
    print(f"Add: {result}")

def subtract(num1,num2):
    result = num1 - num2
    print(f"Subtract: {result}")

def multiply(num1,num2):
    result = num1 * num2
    print(f"Multiply: {result}")

def divide(num1,num2):
    result = num1 / num2
    print(f"Divide: {result}")

num1 = int(input("What's the first number?\n"))
num2 = int(input("What's the second number?\n"))

add(num1,num2)
subtract(num1,num2)
multiply(num1,num2)
divide(num1,num2)