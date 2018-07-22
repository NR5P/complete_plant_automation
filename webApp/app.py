from flask import Flask, render_template
import sys
from automation_controller.IrrigationValve import IrrigationValve
from automation_controller.Timer import Timer
from automation_controller.Lights import Lights
sys.path.append("/home/this/programming/complete_plant_automation/automation_controller")
sys.path.append("/home/this/programming/complete_plant_automation")

app = Flask(__name__)

@app.route("/")
@app.route("/main")
def index():
    return render_template("main.html", Timer=Timer)

@app.route("/valves")
def irrigationValve():
    return render_template("valves.html", IrrigationValve=IrrigationValve)

@app.route("/lights")
def lights():
    return render_template("lights.html", Lights=Lights)


if __name__ == "__main__":
    app.run(debug=True)

