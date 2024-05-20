from flask import Flask, render_template, request, redirect, url_for
from model_current import current_temp, current_description, current_icon, dt_time , name_country
import requests
from config import api_key
from model_forecast import fetch_forecast

app = Flask(__name__)




@app.route('/')
def index():
    forecast_data = fetch_forecast()
    return render_template('index.html', current_temp=current_temp, current_description=current_description,
                            current_icon=current_icon, dt_time=dt_time, name=name_country, forecast_data = forecast_data)



@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    # Формируем запрос к OpenWeather API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    # Возвращаем результат в формате JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)