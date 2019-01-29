from flask import Flask, render_template
import requests

app = Flask(__name__)
app.debug = True


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/parkovi")
def parkovi():
    return render_template("parkovi.html")

@app.route("/plitvice")
def plitvice():

    return render_template("plitvice.html", jsonWeather=getWeather(3188691))

@app.route("/risnjak")
def risnjak():
    return render_template("risnjak.html", jsonWeather=getWeather(3202104))

@app.route("/paklenica")
def paklenica():
    return render_template("paklenica.html", jsonWeather=getWeather(3189964))


def getWeather(id):

    parameters = { 'appid': '7f1839b423ed0ec9c2c366cab3867ca2',
    'id': id, 'units': 'metric', 'lang': 'hr' }
    url = 'https://api.openweathermap.org/data/2.5/weather'
    
    response = requests.get(url, params=parameters)
    
    jsonWeather = response.json()
    
    return jsonWeather

if __name__ == "__main__":
    app.run()
    