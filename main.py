from flask import Flask, render_template, request, session
import requests
from flask_babel import Babel
import json
import random

app = Flask(__name__)
app.debug = True
app.secret_key = 'secret_key'


#prijevod
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/getstarted")
def getstarted():
    return render_template("getstarted.html")

@app.route("/zrmanja")
def zrmanja():
    jsonUserReviewZrmanja = open('./users/users.json').read()
    data = json.loads(jsonUserReviewZrmanja)

    numberOfPeople = len(data)
    listOfNumbers = list()
    randomNum = random.randint(0, (numberOfPeople -1))
    listOfNumbers.append(randomNum)

    while(len(listOfNumbers) < 2):
        randomNum2 = random.randint(0, (numberOfPeople -1))
        if(randomNum2 not in listOfNumbers):
            listOfNumbers.append(randomNum2)

    randomPerson1 = data[listOfNumbers[0]]
    randomPerson2 = data[listOfNumbers[1]]

    return render_template("zrmanja.html", jsonWeather=getWeather(3188691), user1=randomPerson1, user2=randomPerson2)

@app.route("/paklenica")
def paklenica():
    return render_template("paklenica.html", jsonWeather=getWeather(3202104))
    
@app.route("/raftingCalculator")
def raftingCalculator():
    return render_template("raftingCalculator.html")

@app.route("/risnjak")
def risnjak():
    return render_template("risnjak.html", jsonWeather=getWeather(3189964))


def getWeather(id):

    parameters = { 'appid': '7f1839b423ed0ec9c2c366cab3867ca2',
    'id': id, 'units': 'metric', 'lang': 'hr' }
    url = 'https://api.openweathermap.org/data/2.5/weather'
    
    response = requests.get(url, params=parameters)
    
    jsonWeather = response.json()
    
    return jsonWeather

@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'en')

if __name__ == "__main__":
    app.run()
    