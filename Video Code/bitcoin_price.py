import requests
from pprint import pprint

bitcoin_url = ("https://claraj.github.io/mock-bitcoin/currentprice.json")


response = requests.get(bitcoin_url) # getting API data, this is a GET request

data = response.json() # converting the response to a dictionary

pprint(data) # printing the data

dollars_exchange_rate = data["bpi"]["USD"]["rate_float"] # getting the exchange rate for dollars

bitcoin = float(input("How many bitcoins do you have? ")) # asking the user for the amount of bitcoins they have

bitcoin_value = bitcoin * dollars_exchange_rate # calculating the value of the bitcoins in dollars

pprint(f'Your bitcoins are worth ${bitcoin_value:.2f}') # printing the value of the bitcoins in dollars, formatted to 2 decimal places