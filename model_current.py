from datetime import datetime, timezone
import requests
from config import api_key

def get_current_weather(city_name):
    current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=ru&units=metric&appid={api_key}"
    current = requests.get(current_url)
    current_weather = current.json()

    current_temp = int(current_weather.get("main").get("temp"))
    current_feels_like = int(current_weather.get("main").get("feels_like"))
    current_description = current_weather.get("weather")[0].get("description")
    current_icon = current_weather.get("weather")[0].get("icon")
    current_dt = current_weather.get("dt")
    current_sunrise = current_weather.get("sys").get("sunrise")
    current_sunset = current_weather.get("sys").get("sunset")
    sunrise_dt = datetime.fromtimestamp(current_sunrise, timezone.utc)
    sunset_dt = datetime.fromtimestamp(current_sunset, timezone.utc)
    sunrise_time = sunrise_dt.strftime('%H:%M')
    sunset_time = sunset_dt.strftime('%H:%M')
    visibility = current_weather.get('visibility')
    pressure = current_weather.get('main').get('pressure')
    humidity = current_weather.get('main').get('humidity')
    dt = datetime.fromtimestamp(current_dt, timezone.utc)
    dt_time = dt.strftime('%A %d, %B')
    name = current_weather.get("name")
    country = current_weather.get("sys").get("country")
    name_country = f"{name}, {country}"
    

    return {
        "temp": current_temp,
        "description": current_description,
        "icon": current_icon,
        "dt_time": dt_time,
        "name_country": name_country,
        "sunrise": sunrise_time,
        "sunset": sunset_time,
        "feels_like": current_feels_like,
        "visibility": int(visibility / 1000),
        "pressure": int(pressure),
        "humidity": int(humidity)
    }
