from flask import Flask, render_template

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
    return render_template("plitvice.html")

@app.route("/risnjak")
def risnjak():
    return render_template("risnjak.html")

@app.route("/paklenica")
def paklenica():
    return render_template("paklenica.html")

if __name__ == "__main__":
    app.run()
    