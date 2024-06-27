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
        weather = await client.get(random.choice(cities))

        # returns the current day's forecast temperature (int)
        print(f"The weather is {weather.temperature}ºF in {weather.location}")

        # Get the time of day
        #print(weather.datetime) # Still working on formatting the time


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


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())