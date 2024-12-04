from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    quotes = None

    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        quotes = get_quotes()
    return render_template('index.html', weather=weather, quotes=quotes)

def get_weather(city):
    api_key = '389a91f08e0721c361e3c6e23c62a19d'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    response = requests.get(url)
    return response.json()
def get_quotes():
    url = 'https://api.quotable.io/random?limit=1'
    response = requests.get(url, verify=False)
    return response.json()

if __name__ == '__main__':
    app.run()