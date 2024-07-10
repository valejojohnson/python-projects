# This is a python program to let the computer guess
# against itself 10 times until a match is found
# If no match is found, let us know how many tries then exit

import random
import time

# Generate a random answer then print for us to see
answer = random.randint(1, 5)
print(f'The correct answer is: {answer}')
print()

# Initialize the tries starting from 1
tries = 1

# Let the computer guess 10 times then exit
while tries < 10:
    computer_guess = random.randint(1, 5)

    # If the guess doesn't match the answer print the guess then try again
    # and add a number to tries then wait 1 seconds
    if computer_guess != answer:
        print(f"No match with {computer_guess}, trying again")
        tries += 1
        time.sleep(1)

    # If the guess DOES equal answer let us know how many
    # tries it took, then break out of the loop
    elif computer_guess == answer:
        print()
        print(f"We MATCHED at {computer_guess} after {tries} tries")
        break

# If there are no matches after 10 tries just let us know
else:
    print(f"No matches after {tries} tries")
