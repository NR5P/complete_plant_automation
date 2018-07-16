from flask import Flask, render_template
from Timer import Timer


app = Flask(__name__)

@app.route("/")
@app.route("/main")
def index():
    return render_template("main.html")

@app.route("/valves")
def irrigationValve():
    return render_template("valves.html", Timer=Timer)

@app.route("/lights")
def lights():
    return render_template("lights.html")


if __name__ == "__main__":
    app.run(debug=True)

