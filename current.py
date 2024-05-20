import requests

api_key = '0185c3d00094d09af383254afbb760f4'

# Получение данных с сервера
def fetch_data(url, callback):
    response = requests.get(f"{url}&appid={api_key}")
    data = response.json()
    callback(data)

# URL-адреса для запросов
class URL:
    @staticmethod
    def current_weather(lat, lon):
        return f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=ru&units=metric&appid={api_key}"

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


def fetchData(lat, lon, callback):
    url = URL.current_weather(lat, lon)
    response = requests.get(url)
    try:
        response.raise_for_status()  # Check if the request was successful
        currentWeather = response.json()
        weather = currentWeather['weather'][0]
        dateUnix = currentWeather['dt']
        sunriseUnixUTC = currentWeather['sys']['sunrise']
        sunsetUnixUTC = currentWeather['sys']['sunset']
        temp = currentWeather['main']['temp']
        feels_like = currentWeather['main']['feels_like']
        pressure = currentWeather['main']['pressure']
        humidity = currentWeather['main']['humidity']
        visibility = currentWeather.get('visibility', None)  # Use .get() to handle missing key
        timezone = currentWeather['timezone']
        description = weather['description']
        icon = weather['icon']
        card = {'weather': weather, 'dateUnix': dateUnix, 'sunriseUnixUTC': sunriseUnixUTC,
                'sunsetUnixUTC': sunsetUnixUTC, 'temp': temp, 'feels_like': feels_like,
                'pressure': pressure, 'humidity': humidity, 'visibility': visibility,
                'timezone': timezone, 'description': description, 'icon': icon}
        callback(card)
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
    except KeyError as e:
        print("Key error:", e)
        print("Response content:", response.text)

# Пример использования
def callback_function(data):
    print(data)

fetchData(40.7128, -74.0060, callback_function)  # Пример координат Нью-Йорка