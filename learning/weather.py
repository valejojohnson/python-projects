import random
import time
import os


def clear_screen():
    """Clears the console screen."""
    if 'TERM' not in os.environ:
        os.environ['TERM'] = 'xterm'

    os.system('cls' if os.name == 'nt' else 'clear')


def get_temperature_description(number):
    """Returns a descriptive string based on the temperature value."""
    if number < 32:
        return 'freezing'
    elif number > 95:
        return 'scorching'
    else:
        return 'nice'


def generate_random_number_and_city():
# Generates and returns a string describing the temperature in a randomly chosen city.

    cities = [
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
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
    number = random.randint(-10, 115)
    city = random.choice(cities)
    temperature_description = get_temperature_description(number)
    return f"In the city of {city}, it's a {temperature_description} {number}°F"

# Run the loop for 20 seconds, clearing the screen and printing new output every 2 seconds


start_time = time.time()
while time.time() - start_time < 20:
    clear_screen()  # Clear the screen before printing new output
    print(generate_random_number_and_city())
    time.sleep(2)  # Pause the execution for 2 seconds
