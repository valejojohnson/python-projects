from datetime import datetime


def get_time():
    # Get the current local hour
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
