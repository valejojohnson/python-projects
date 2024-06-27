# This python code is designed to greet a user
# the proper salutation based on local time

# Importing datetime as this will help us get the hour of day
from datetime import datetime

# Function to get the time of day and if hour
# is less than Noon print Good Morning
# else print Good Evening
def get_time():
    # Get the current local time
    current_hour = datetime.now().time()

    # If before Noon, return Good Morning, anything else Good Evening
    if current_hour.hour < 12:
        return 'Good Morning'
    else:
        return 'Good Evening'


# Ask for users first name
name = input("What's your first name? ")

# Call the get_time function to get proper salutation
salutation = get_time()

# Using the salutation that was pulled from get_time function, then capitalize the first name (if it wasn't already)
print(f'{salutation}, {name.capitalize()}')
