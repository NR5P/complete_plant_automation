from flask import Flask, render_template, request, flash, jsonify
import sys
from automation_controller.IrrigationValve import IrrigationValve
from automation_controller.Timer import Timer
from automation_controller.Lights import Lights
from .jinja_filters import *
from webApp.forms import ValveForm
sys.path.append("/home/this/programming/complete_plant_automation/automation_controller")
sys.path.append("/home/this/programming/complete_plant_automation")


app = Flask(__name__)
app.config["SECRET_KEY"] = "thisisasecretkey"

app.jinja_env.filters['strf_time_converter'] = strf_time_converter
app.jinja_env.filters['deltaToHrMinSec'] = deltaToMinSec

app.jinja_env.filters["strftimeConverter"] = strf_time_converter
app.jinja_env.filters["HrMinSec"] = deltaToHrMinSec
app.jinja_env.filters["HrMin"] = deltaToHrMin
app.jinja_env.filters["MinSec"] = deltaToMinSec
app.jinja_env.filters["trueFalseIndicator"] = trueFalseIndication

@app.route("/")
@app.route("/main")
def index():
    return render_template("main.html", Timer=Timer)

@app.route("/valves", methods=["GET", "POST"])
def irrigationValve():
    formList = [ValveForm() for i in range(10)]
    for form in formList:
        if form.validate_on_submit():
            form.setValve(irrigationValve.valveList[form])
            flash("changes saved", "success")
    return render_template("valves.html", IrrigationValve=IrrigationValve, formList=formList)

@app.route("/lights")
def lights():
    return render_template("lights.html", Lights=Lights)

@app.route("/api/<component>")
def componentApi():
    """
    api for each template. 
    """
    return render_template("{component}.html")



def startApp():
    app.run(host='0.0.0.0',port=5000)


if __name__ == "__main__":
    startApp()

