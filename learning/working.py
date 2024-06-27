# Put my imports here
import random
import time


# Start coding here
def get_user_name():
    firstname = input(f'Hi, whats your FIRST Name? ')
    print('')

    lastname = input(f'Hi {firstname.capitalize()}, what''s your LAST Name? ')
    print('')

    name = f'{firstname.capitalize()} {lastname.capitalize()}'

    print(f'Great! I have your full name as {name} ')
    print('')

    return firstname


def rand_age(firstname):

    # Put in the basic variables
    current_year = time.localtime().tm_year

    # Allow user to put in year then store in variable
    birth_year = random.randint(1900, 2023)

    # Do the math to get the current age using the age variable
    age = current_year - int(birth_year)

    # Output the age variable
    print(f'{firstname.capitalize()}, your age would be {age} if you were born in {birth_year}')
    print('')

    return


rand_age(firstname=get_user_name())
