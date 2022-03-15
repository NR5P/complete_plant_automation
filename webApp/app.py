from flask import Flask, render_template, request, flash, jsonify, redirect, url_for
import sys, os, json
from jinja_filters import *
from db import DB
db = DB()
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

@app.route("/api/getallcycleirrigation", methods=['GET'])
@app.route("/api/getallcycleirrigation/<int:id>", methods=['GET'])
def returnAllCycleIrrigation(id = None):
    """
    returns all cycle components
    """
    try:
        if id != None and id.isdigit():
            cycleIrrigationComponents = db.getAllCycleIrrigationTimes(id)
        else:
            cycleIrrigationComponents = db.getAllCycleIrrigationTimes()
        cycleList = []
        if cycleIrrigationComponents != None and len(cycleIrrigationComponents) > 0:
            cycleList = [x.toDict() for x in cycleIrrigationComponents]
            return json.dumps(cycleList)
        else:
            return ""
    except Exception as e:
        print("exception returning cylcleList: " + str(e))

@app.route("/api/getalltimedirrigation", methods=['GET'])
@app.route("/api/getalltimedirrigation/<int:id>", methods=['GET'])
def returnAllTimedIrrigation(id = None):
    """
    returns all timed components
    """
    try:
        if id == None:
            timeIrrigationComponents = db.getAllTimedIrrigationTimes()
        else:
            timeIrrigationComponents = db.getAllTimedIrrigationTimes(id)
        timedList = [x.toDict() for x in timeIrrigationComponents]
        return json.dumps(timedList)
    except Exception as e:
        print(e)

@app.route("/addnew/<type>", methods=['GET'])
def addNewComponent(type):
    """
    for adding new components.
    """
    if (type == "cycleirrigation"):
        return render_template("addcycleirrigation.html")
    elif (type == "timedirrigation"):
        return render_template("addtimedirrigation.html")

@app.route("/addnew/<type>", methods=['POST'])
def addNewComponentPost(type):
    """
    for adding new components.
    """
    if (type == "cycleirrigation"):
        return render_template("main.html")
    elif (type == "timedirrigation"):
        return render_template("main.html")


def startApp():
    app.run(host='0.0.0.0',port=5000)


if __name__ == "__main__":
    startApp()

