from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

def irrigationValve():
    return render_template("valve.html")

def lights():
    return render_template("lights.html")

