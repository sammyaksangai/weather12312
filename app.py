import requests
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['DEBUG'] = True





@app.route('/', methods=['GET', 'POST'])
def index():
    #if request.method == 'POST':
    new_city = request.form.get('city')
        
        #if new_city:
            #new_city_obj = City(name=new_city)

           

    #cities = City.query.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=86c44ea71a2b79e5563f4274073a145a'

    weather_data = []

    #for city in cities:

    r = requests.get(url.format(new_city)).json()

    weather = {
        'city' : new_city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
        }

    weather_data.append(weather)


    return render_template('weather.html', weather_data=weather_data)
