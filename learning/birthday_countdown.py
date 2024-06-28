# This code is designed to get the current local time
# and get time difference until a birthday

import datetime

# Get the current local time
current_time = datetime.datetime.now()

# Set a birthday of January 17, 2025
birthday = datetime.datetime(2025, 1, 17)

# Subract current time from birthday
time_until = birthday - current_time

print(f'Current local time is: {current_time}')
print()
print(f'Upcoming Birthday is: {birthday}')
print()
print(f'Days until next birthday: {time_until.days}')