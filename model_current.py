from config import api_key
from datetime import datetime, timezone
import requests

current_url = f"https://api.openweathermap.org/data/2.5/weather?q=Волжский&lang=ru&units=metric&appid={api_key}"
current = requests.get(current_url)
current_weather = current.json()
current_temp = int(current_weather.get("main").get("temp"))
current_description = current_weather.get("weather")[0].get("description")
current_icon = current_weather.get("weather")[0].get("icon")
current_dt = current_weather.get("dt") # Получаем текущую дату
dt = datetime.fromtimestamp(current_dt, timezone.utc) # Преобразуем дату в формат datetime
dt_time = dt.strftime('%A %d, %B') # Преобразуем дату в строковый формат
name = current_weather.get("name")
country = current_weather.get("sys").get("country")
name_country = name + ", " + country
