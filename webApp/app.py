from flask import Flask, render_template, request, flash, jsonify, redirect, url_for
import sys, os, json
from automation_controller.Timer import Timer
from automation_controller.heater import Heater
from automation_controller.cycleIrrigation import CycleIrrigation
from automation_controller.fan import Fan
from automation_controller.humidifier import Humidifier
from automation_controller.IrrigationValve import IrrigationValve
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

@app.route("/", methods=['GET'])
def mainPage():
    return render_template("main.html")

@app.route("/settings", methods=['GET'])
def settings():
    return render_template("settings.html")

@app.route("/api", methods=['GET'])
def returnAll():
    """
    returns all components in json file
    """
    try:
        with open("/home/pi/components.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except:
        return "file aint working"

@app.route("/api", methods=['POST'])
def addToJson():
    if request.json["type"] == "cycleirrigation":
        CycleIrrigation.addToJson(request)
    elif request.json["type"] == "irrigationvalve":
        IrrigationValve.addToJson(request)
    elif request.json["type"] == "fan":
        Fan.addToJson(request)
    elif request.json["type"] == "heater":
        Heater.addToJson(request)
    elif request.json["type"] == "light":
        Lights.addToJson(request)
    elif request.json["type"] == "humidifier":
        Humidifier.addToJson(request)

    # return all of the componenents
    return redirect(url_for("returnAll")) 

@app.route("/api/<name>", methods=['PUT'])
def updateJson(name):
    if request.json["type"] == "cycleirrigation":
        CycleIrrigation.updateJson(request, name)
    elif request.json["type"] == "irrigationvalve":
        IrrigationValve.updateJson(request, name)
    elif request.json["type"] == "fan":
        Fan.updateJson(request, name)
    elif request.json["type"] == "heater":
        Heater.updateJson(request, name)
    elif request.json["type"] == "light":
        Lights.updateJson(request, name)
    elif request.json["humidifier"] == "humidifier":
        Humidifier.updateJson(request, name)

    # return all of the componenents
    return redirect(url_for("returnAll")) 

@app.route("/api/<name>", methods=['DELETE'])
def removeJson(name):
    try:
        with open("/home/pi/components.json", "r") as f:
            data = json.load(f) # load the json file into a dictionary
    except:
        pass

    component = [i for i in data if data["name"] == name]
    data.remove(component[0])

    # write the dictionary to json file
    jsonData = json.dumps(data, default=str)
    jsonFile = open("/home/pi/components.json", "w")
    jsonFile.write(jsonData)
    jsonFile.close()

    return redirect(url_for("returnAll"))

@app.route("/api/<name>", methods=['GET'])
def returnOneComponentType(name):
    """
    returns json data from file that is of type in url, dynamically obtained 
    """
    try:
        with open("/home/pi/components.json", "r") as f:
            data = json.load(f)
    except:
        return "file aint working"
    component = [i for i in data if data["type"] == name]
    return jsonify(component)

@app.route("/addnew/<type>")
def addNewComponent(type):
    """
    for adding new components.
    """
    if (type == "cycleirrigation"):
        return render_template("addcycleirrigation.html")
    elif (type == "timedirrigation"):
        return render_template("addtimedirrigation.html")
    elif (type == "light"):
        return render_template("addlight.html")
    elif (type == "fan"):
        return render_template("addfan.html")
    elif (type == "heater"):
        return render_template("addheater.html")
    elif (type == "humidifier"):
        return render_template("addhumidifier.html")

def startApp():
    app.run(host='0.0.0.0',port=5000)


if __name__ == "__main__":
    startApp()

