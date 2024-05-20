from config import api_key
import requests


# forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q=Волжский&units=metric&appid={api_key}'
# forecast = requests.get(forecast_url)
# forecast_weather = forecast.json()

# for index, weather_data in enumerate(forecast_weather.get('list', [])):
#         if index > 7:
#                 break
#         temp = weather_data.get('main', {}).get('temp')
#         wind = weather_data.get('wind', {}).get('speed')
#         dt_txt = weather_data.get('dt_txt')
#         index_weather = ( f'Temperature: {temp}, Wind Speed: {wind}, Date: {dt_txt}')
#         print(index_weather)

def fetch_forecast():
    forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q=Волжский&units=metric&appid={api_key}'
    forecast = requests.get(forecast_url)
    forecast_weather = forecast.json()
    forecast_data = []
    for index, weather_data in enumerate(forecast_weather.get('list', [])):
        if index > 5:
            break
        time = weather_data.get('dt_txt').split()[1][:5]
        temp = weather_data.get('main', {}).get('temp')
        wind_speed = weather_data.get('wind', {}).get('speed')
        forecast_data.append({'time': time, 'temp': temp, 'wind_speed': wind_speed})
    return forecast_data