import pandas as pd
import requests
import os

# Extracting data from the OpenWeatherMap API

def extract_weather_data(city_name):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'

    res = requests.get(url)
    res.raise_for_status() # checks status codes
    raw_weather_data = res.json()

    return raw_weather_data

# print(extract_weather_data('boston'))