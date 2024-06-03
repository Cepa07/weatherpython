from flask import Flask, render_template, request
from config import api_key
from model_current import get_current_weather
from model_forecast import fetch_forecast
from days import weather_days

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    city_name = "Moscow" 
    if request.method == 'POST':
        city_name = request.form['city']

    current_weather = get_current_weather(city_name)
    forecast_data = fetch_forecast(city_name)
    forecast_days = weather_days(city_name)
    
    return render_template('index.html',
                           current_temp=current_weather['temp'],
                           current_description=current_weather['description'],
                           current_icon=current_weather['icon'],
                           dt_time=current_weather['dt_time'],
                           name=current_weather['name_country'],
                           sunrise = current_weather['sunrise'],
                           sunset = current_weather['sunset'],
                           forecast_data=forecast_data,
                           feels_like = current_weather['feels_like'],
                           visibility = current_weather['visibility'],
                           pressure = current_weather['pressure'],
                           humidity = current_weather['humidity'],
                           forecast_days = forecast_days,
                           )

if __name__ == '__main__':
    app.run(debug=True)
