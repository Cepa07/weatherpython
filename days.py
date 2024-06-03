import requests
from config import api_key
from datetime import datetime

def weather_days(city_name):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
    weather_forecast = []
    unique_dates = set()
    
    for entry in data['list']:
        date_str = entry['dt_txt']
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        
        if date.strftime('%Y-%m-%d') not in unique_dates and date.hour == 12:  # выбираем прогноз на полдень каждого дня
            weather_data = {
                'date': date.strftime('%d %b'),
                'day_of_week': date.strftime('%A'),
                'temperature': entry['main']['temp_max'],
                'description': entry['weather'][0]['description'],
                'icon': entry['weather'][0]['icon']
            }
            weather_forecast.append(weather_data)
            unique_dates.add(date.strftime('%Y-%m-%d'))
        
        if len(weather_forecast) == 5:  # ограничиваем прогноз 5 днями
            break
    
    return weather_forecast

# Example usage:
if __name__ == '__main__':
    city_name = "Moscow"
    forecast = weather_days(city_name)
    for day in forecast:
        print(day)
