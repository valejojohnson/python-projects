name = input(str("Hi, what's your FIRST name? ")).capitalize()
age = int(input("How old are you? "))

if age <= 17:
    print(f"We're sorry, {name}, you aren't old enough to be here at {age}")
elif age <= 30:
    print(f'Welcome to your holiday, {name}! We really hope you enjoy your time here')
else:
    print(f"Sorry, {name}. You're too old to be here")
