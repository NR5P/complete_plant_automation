from flask import Flask, render_template, request
import sys
from automation_controller.IrrigationValve import IrrigationValve
from automation_controller.Timer import Timer
from automation_controller.Lights import Lights
from .jinja_filters import *
sys.path.append("/home/this/programming/complete_plant_automation/automation_controller")
sys.path.append("/home/this/programming/complete_plant_automation")

app = Flask(__name__)


app.jinja_env.filters["strftimeConverter"] = strf_time_converter
app.jinja_env.filters["HrMinSec"] = deltaToHrMinSec
app.jinja_env.filters["HrMin"] = deltaToHrMin
app.jinja_env.filters["MinSec"] = deltaToMinSec
app.jinja_env.filters["trueFalseIndicator"] = trueFalseIndication

@app.route("/")
@app.route("/main")
def index():
    return render_template("main.html", Timer=Timer)

@app.route("/valves")
def irrigationValve():
    return render_template("valves.html", IrrigationValve=IrrigationValve)

#@app.route("/send", methods=["GET", "POST"])
#def send():
#    if request.method == "POST":
#        pass

@app.route("/lights")
def lights():
    return render_template("lights.html", Lights=Lights)


#if __name__ == "__main__":

def startApp():
    app.run(host='0.0.0.0',port=5000)

