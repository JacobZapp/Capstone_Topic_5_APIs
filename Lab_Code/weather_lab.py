import os
import requests
from pprint import pprint


# Minneapolis
lat = 44.97
lon = -93.26
units = 'imperial'  # change to 'imperial' for quantities in Fahrenheit, miles per hour etc.

# error here can be non existent key, expired key, etc. this catches errors but does no display what the error is.
# Get the API key from the environment variable, and if there is not one, show error and exit
try:
    api_key = os.environ['WEATHER_KEY']  # Set this environment variable on your computer
except KeyError:
        print("Error: Please set the WEATHER_KEY environment variable.")
        exit(1)

url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}'

# different things can go wrong here, no connection, faulty api format, incorrecnt url
# if the request fails, print the error and exit
try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
    exit(1)

weather_forecast = response.json()

print (f"Weather forecast for Minneapolis, MN:")
for forecast in weather_forecast["list"]:
    timestamp = forecast["dt_txt"]
    temperature = forecast["main"]["temp"]
    description = forecast["weather"][0]["description"]
    wind_speed = forecast["wind"]["speed"]

    print('---')
    print(f'Date and Time: {timestamp}')
    print(f'Temperature: {temperature}°F')
    print(f'Weather Description: {description}')
    print(f'Wind Speed: {wind_speed} mph')
    print('---')


