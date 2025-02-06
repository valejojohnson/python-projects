# This script will get a name input, and call the function to give a salutation to that name


def salutation(name):
    return print(f"Welcome to Avalon, {name.capitalize()}")


name = str(input("What's your first name?\n"))
salutation(name) # Call the other function using the variable created

