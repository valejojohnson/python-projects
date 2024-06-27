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
        print("The weather is",weather.temperature,'in',weather.location)


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
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())