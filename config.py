import requests

api_key = '0185c3d00094d09af383254afbb760f4'

# Получение данных с сервера
"""def fetch_data(URL, callback):
    response = requests.get(f"{URL}&appid={api_key}")
    data = response.json()
    callback(data)

# URL-адреса для запросов
class URL:
    @staticmethod
    def current_weather(lat, lon):
        return f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=ru&units=metric"

    @staticmethod
    def forecast(lat, lon):
        return f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric"

    @staticmethod
    def air_pollution(lat, lon):
        return f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}"

    @staticmethod
    def reverse_geo(lat, lon):
        return f"https://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=5"

    @staticmethod
    def geo(query):
        return f"https://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5"
"""