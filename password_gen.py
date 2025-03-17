import random
import string

length = 12
password = ''.join(random.choices(string.hexdigits,k=length))

print(password)