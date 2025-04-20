from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['location']['name'],
                'temperature': data['current']['temp_c'],
                'description': data['current']['condition']['text'],
                'humidity': data['current']['humidity'],
                'wind': data['current']['wind_kph']
            }
        else:
            weather_data = {'error': 'City not foundss or API issue'}
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
