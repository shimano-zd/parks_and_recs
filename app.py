from flask import Flask, render_template, request, session
import requests
from flask_babel import Babel
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email
import json
import random

app = Flask(__name__)

app.secret_key = 'secret_key'


#prijevod
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

babel = Babel(app)

# forma i provjera unosa
class LoginForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min=3, message="Please enter at least 3 characters")])
    email = StringField('email', validators=[InputRequired(), Email("This field requires a valid email address")])
    

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/subscribe", methods=['GET','POST'])
def subscribe():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template("subscribe.html", form = form, message='Great, check your email!')
    return render_template("subscribe.html", form=form)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/getstarted")
def getstarted():
    return render_template("getstarted.html")

# zrmanja i paklenica dobivaju podatke o korisnicima iz jsona u root direktoriju
# funkcija getRandomPeople() odabira nasumicne ljude i salje u view

@app.route("/zrmanja")
def zrmanja():
    jsonUserReviewZrmanja = open('./users/usersZrmanja.json').read()
    data = json.loads(jsonUserReviewZrmanja)

    userTuple = getRandomPeople(data)

    user1 = userTuple[0]
    user2 = userTuple[1]
    
    # 3194245 je Obrovac
    return render_template("zrmanja.html", jsonWeather=getWeather(3194245), user1=user1, user2=user2)

@app.route("/paklenica")
def paklenica():

    jsonUserReviewPaklenica = open('./users/usersPaklenica.json').read()
    data = json.loads(jsonUserReviewPaklenica)

    userTuple = getRandomPeople(data)

    user1 = userTuple[0]
    user2 = userTuple[1]

    # 3189964 je Starigrad

    return render_template("paklenica.html", jsonWeather=getWeather(3189964), user1=user1, user2=user2)

def getRandomPeople(data):
    numberOfPeople = len(data)
    listOfNumbers = list()
    randomNum = random.randint(0, (numberOfPeople-1))
    listOfNumbers.append(randomNum)

    # petlja sluzi sprjecavanju unosa istog korisnika dva puta
    while(len(listOfNumbers) < 2):
        randomNum2 = random.randint(0, (numberOfPeople-1))
        if(randomNum2 not in listOfNumbers):
            listOfNumbers.append(randomNum2)

    randomPerson1 = data[listOfNumbers[0]]
    randomPerson2 = data[listOfNumbers[1]]
    randomPersonTuple = [randomPerson1,randomPerson2]

    return randomPersonTuple

# kalkulatori za izracun cijena
@app.route("/raftingCalculator")
def raftingCalculator():
    return render_template("raftingCalculator.html")
@app.route("/climbingCalculator")
def climbingCalculator():
    return render_template("climbingCalculator.html")

# error handleri

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

# dohvat podataka o vremenu
def getWeather(id):

    parameters = { 'appid': '7f1839b423ed0ec9c2c366cab3867ca2',
    'id': id, 'units': 'metric', 'lang': 'hr' }
    url = 'https://api.openweathermap.org/data/2.5/weather'
    
    response = requests.get(url, params=parameters)
    
    jsonWeather = response.json()
    
    return jsonWeather



if __name__ == "__main__":
    app.run()
    