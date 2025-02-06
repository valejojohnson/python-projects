# Use a while loop to print text until a certain number is reached
import random

i = 0
max = random.randint(0,50)
print(f"Max is {max}")

while i < max:
    print(i)
    i += 1
