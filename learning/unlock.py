# This app will mimic the Tesla Funk opening codebase
# Based on distance, if too far ask if user is sure to open
# If within safe distance, open without question

import random # For generating a random distance

distance = int(random.randint(0,150))

if distance > 50:
    response = input(f"Distance: {distance}ft - Are you sure you'd like to open the Frunk?\n")
    if response.casefold() == "y":
        print("Your Frunk has been opened")
    else:
        print("Bad input, your Frunk is still closed and secured")
else:
    print(f"Distance: {distance}ft - Your Frunk has been opened")
