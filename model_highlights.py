import requests
from config import api_key

highlight_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=ru&units=metric&appid={api_key}"