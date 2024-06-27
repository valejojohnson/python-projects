# This python code will generate a random city from a list,
# then generate a random number for the temp then classify
# based on temp generated how the weather feels

import random  # To get a random temp later
import time  # Sleep between runs
import os  # Used to let us clear screen based on OS


# Clear screen after every time evolution of code run
def clear_screen():
    """Clears the console screen."""
    if 'TERM' not in os.environ:
        os.environ['TERM'] = 'xterm'

    os.system('cls' if os.name == 'nt' else 'clear')


# Create a description of weather feel based on temp generated
def get_temperature_description(temp):
    """Returns a descriptive string based on the temperature value."""
    if temp < 32:
        return 'freezing'
    elif temp > 95:
        return 'scorching'
    else:
        return 'nice'


# Pull a random city, generate a random number for temp then print how it
# feels in random city with random temp.
def generate_random_number_and_city():
    # Generates and returns a string describing the temperature in a randomly chosen city.

    cities = [
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia",
        "San Antonio", "San Diego", "Dallas", "San Jose",
        "London", "Manchester", "Birmingham", "Leeds", "Glasgow",
        "Tokyo", "Osaka", "Nagoya", "Sapporo", "Fukuoka",
        "Paris", "Marseille", "Lyon", "Toulouse", "Nice",
        "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide",
        "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai",
        "Cairo", "Alexandria", "Giza", "Luxor", "Aswan",
        "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu",
        "Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Nizhny Novgorod",
        "São Paulo", "Rio de Janeiro", "Salvador", "Brasilia", "Fortaleza",
        "Cape Town", "Johannesburg", "Durban", "Pretoria", "Port Elizabeth",
        "Mexico City", "Guadalajara", "Monterrey", "Puebla", "Toluca",
        "Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza",
        "Rome", "Milan", "Naples", "Turin", "Palermo",
        "Istanbul", "Ankara", "Izmir", "Bursa", "Antalya",
        "Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton",
        "Dubai", "Abu Dhabi", "Sharjah", "Al Ain", "Ajman"
    ]
    temp = random.randint(-10, 115)
    city = random.choice(cities)
    temperature_description = get_temperature_description(temp)
    return f"In the city of {city}, it's a {temperature_description} {temp}°F"


# Run the loop for 20 seconds, clearing the screen and printing new output every 2 seconds
start_time = time.time()
while time.time() - start_time < 20:
    clear_screen()  # Clear the screen before printing new output
    print(generate_random_number_and_city())
    time.sleep(3)  # Pause the execution for 2 seconds
