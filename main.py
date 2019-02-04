from flask import Flask, render_template, request, session
import requests
<<<<<<< HEAD
from flask_babel import Babel
import json
import random

app = Flask(__name__)
app.debug = True
app.secret_key = 'secret_key'


#prijevod
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
=======
from flask_bootstrap import Bootstrap
from flask_babel import Babel

app = Flask(__name__)
app.debug = True
bootstrap = Bootstrap(app)
app.secret_key = 'NEKA_ŽVRLJOTINA'

app.config['BABEL_DEFAULT_LOCALE'] = 'hr'
>>>>>>> a22af8c03517cb20b9efa45e1fa2c9a122974671
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


@app.route("/smjestaj")
def smjestaj():
    return render_template("smjestaj.html")

@app.route("/novosti")
def novosti():
    return render_template("novosti.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang','en')

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
    