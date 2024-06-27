# This code is designed to take input for first name and age
# If age is less than 18 print that they're too young
# if age is older than 31, print they're too old to be here

# Initialize the name and age variables by asking user for input
name = input(str("Hi, what's your FIRST name? ")).capitalize()
age = int(input(f"How old are you, {name}? "))

# Calculate difference in age if too young
difference = 18 - age

# If age is less than 18 tell user they're too young and to come back
# after the difference in years
if age <= 17:
    print(f"We're sorry, {name}, you aren't old enough to be here at {age}. Come back in {difference} years")
# If user age is within range, welcome them to holiday
elif age <= 30:
    print(f'Welcome to your holiday, {name}! We really hope you enjoy your time here')
# If older than 30, print user is too old
else:
    print(f"Sorry, {name}. You're too old to be here")
