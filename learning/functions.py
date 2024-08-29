# Create a calculator here in python

def multiply(a, b):
    result = a * b
    return result


def add(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


def divide(a, b):
    result = a / b
    return result


answer = ''
a = int(input('Input the first number '))
b = int(input('Input the second number '))

to_do = input('What do you want to do with these numbers? (Ex. add +, subtract -, divide /, multiply *) ')

if to_do == 'add' or to_do == '+':
    answer = add(a, b)
    print(f'These numbers added = {answer}')
elif to_do == 'subtract' or to_do == '-':
    answer = subtract(a, b)
    print(f'These numbers subtracted = {answer}')
elif to_do == 'divide' or to_do == '/':
    answer = divide(a, b)
    print(f'These numbers divided = {answer}')
elif to_do == 'multiply' or to_do == '*':
    answer = multiply(a, b)
    print(f'These numbers multiplied = {answer}')
else:
    print('Please enter something to do with the numbers (Ex. add +, subtract -, divide /, multiply *) ')