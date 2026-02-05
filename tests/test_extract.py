import pytest
import requests
import os
# from etl import extract

def test_api_key():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    assert api_key is not None

def test_extract_weather_data():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city = "boston"
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    
    res = requests.get(url)
    
    assert res.status_code == 200
    
    data = res.json()
    assert isinstance(data, dict)