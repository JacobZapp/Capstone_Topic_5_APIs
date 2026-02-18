import requests



response = requests.get("https://catfact.ninja/fact") # getting the dat afrom the API, this is a GET request, we can also do POST, PUT, DELETE etc.

print(response.status_code) # gives the status codes, differents 100's means different errors

response.raise_for_status() # raise an exception for 400 or 500 status codes
print(response.text)
print(response.json())

data = response.json()

fact = data["fact"]
print(f'A random fact about cats: {fact}')