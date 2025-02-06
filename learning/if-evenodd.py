# Determine if number is Even/Odd

import random
num = int(random.randint(0,450))

if num % 2 == 0:
    print(f"{num} is Even")
elif num % 2 == 1:
    print(f"{num} is Odd")
else:
    print(f"{num} isn't a number")