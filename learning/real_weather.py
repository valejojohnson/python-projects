# This python is to pull a random city from the list
# then pull the current temperature in said city
# then print the output.

import python_weather
import asyncio
import os
import random
from datetime import datetime


async def getweather():
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # fetch a weather forecast from a random city listed below
        weather = await client.get(random.choice(american_cities))
        clear_screen()

        # returns the current day's forecast temperature (int)
        print(f"The weather is {weather.temperature}ºF in {weather.location}")

        # Get the time of day
        # print(weather.datetime) # Still working on formatting the time


def clear_screen():
    """Clears the console screen."""
    if 'TERM' not in os.environ:
        os.environ['TERM'] = 'xterm'

    os.system('cls' if os.name == 'nt' else 'clear')



american_cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
    "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington",
    "Boston", "El Paso", "Nashville", "Detroit", "Oklahoma City",
    "Portland", "Las Vegas", "Memphis", "Louisville", "Baltimore",
    "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento",
    "Kansas City", "Long Beach", "Mesa", "Atlanta", "Colorado Springs",
    "Virginia Beach", "Raleigh", "Omaha", "Miami", "Oakland",
    "Minneapolis", "Tulsa", "Wichita", "New Orleans", "Arlington",
    "Cleveland", "Bakersfield", "Tampa", "Aurora", "Honolulu",
    "Anaheim", "Santa Ana", "Corpus Christi", "Riverside", "Lexington",
    "St. Louis", "Stockton", "Pittsburgh", "Saint Paul", "Cincinnati",
    "Anchorage", "Henderson", "Greensboro", "Plano", "Newark",
    "Lincoln", "Toledo", "Orlando", "Chula Vista", "Irvine",
    "Fort Wayne", "Jersey City", "Durham", "St. Petersburg", "Laredo",
    "Buffalo", "Madison", "Lubbock", "Chandler", "Scottsdale",
    "Glendale", "Reno", "Norfolk", "Winston-Salem", "North Las Vegas",
    "Irving", "Chesapeake", "Gilbert", "Hialeah", "Garland",
    "Fremont", "Richmond", "Boise", "San Bernardino"
]

if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())