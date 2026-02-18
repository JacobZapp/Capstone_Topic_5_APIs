import requests
from pprint import pprint
import os

key = os.environ.get("WEATHER_KEY") # getting the API key from the environment variable

url = f'https://api.openweathermap.org/data/2.5/weather?q=tokyo,jp&units=imperial&appid={key}'

city = input("Enter a city name: ") # asking the user to input a city name
country = input("Enter a country code (e.g. 'us' for United States): ") # asking the user to input a country code
location = f"{city},{country}" # creating a string for the location in the format "city,country"

query = {'q': location, 'units': 'imperial', 'appid': key} # creating a dictionary for the query parameters

data = requests.get(url, params=query).json() # getting info from url and turning it as a json object

pprint(data) # printing the data

temperature = data["main"]["temp"] # getting the temperature, the main is the key for the main data, and temp is the key for the temperature in that data
pprint(f'The current temperature in {location} is {temperature} degrees Fahrenheit.')