import requests
from datetime import datetime
from config import API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    return {
        "city": city,
        "country": data["sys"]["country"],
        "lat": data["coord"]["lat"],
        "lon": data["coord"]["lon"],
        "timestamp": datetime.now(),
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind": data["wind"]["speed"],
        "condition": data["weather"][0]["description"]
    }