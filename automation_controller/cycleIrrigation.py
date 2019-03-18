"""
for cycle irrigation like for propagating plants. takes on time, off time, and a blackout time. typically 
for short bursts of irrigation
"""

from .Timer import Timer

import time
import datetime
import RPi.GPIO as GPIO
import json

class CycleIrrigation(Timer):
    def __init__(self):

        self.cycleOnTime = None
        self.cycleOffTime = None
        self.blackoutStart = None
        self.blackoutStop = None
        self.componentData = self.save()

    def run(self):
        pass
    
    def save(self):
        self.componentData = {"type" : "cycle",
                              "name" : self.name,
                              "pin"  : self.pin,
                              "on"   : self.on,
                              "currentlyOn" : self.currentStateOn,
                              "test" : self.test,
                              "notes": self.notes,
                              "blackoutStart" : self.blackoutStart,
                              "blackoutStop" : self.blackoutStop}
        self.addToJson(componentData)

    @staticmethod
    def addToJson(request):
        try:
            with open("/home/pi/components.json", "r") as f:
                data = json.load(f) # load the json file into a dictionary
        except:
            pass
        componentData = {
            "componentType" : request.json["type"],
            "name" : request.json["name"],
            "pin" : request.json["pin"],
            "on" : request.json["on"],
            "test" : request.json["test"],
            "currentStateOn" : request.json["currentStateOn"],
            "notes" : request.json["notes"],
            "cycleOnTime" : request.json["cycleOnTime"],
            "cycleOffTime" : request.json["cycleOffTime"],
            "blackoutStart" : request.json["blackoutStart"],
            "blackoutStop" : request.json["blackoutStop"],
        }

        # append to dictionary of json data
        data.append(componentData)

        # write the dictionary to json file
        jsonData = json.dumps(data, default=str)
        jsonFile = open("/home/pi/components.json", "w")
        jsonFile.write(jsonData)
        jsonFile.close()
        
@staticmethod
def updateJson(request, name):
    try:
        with open("/home/pi/components.json", "r") as f:
            data = json.load(f) # load the json file into a dictionary
    except:
        pass

    component = [i for i in data if data["name"] == name]
    # if the name is already in replace the values
    component[0]["type"] = request.json["type"]
    component[0]["name"] = request.json["name"]
    component[0]["pin"] = request.json["pin"]
    component[0]["on"] = request.json["on"]
    component[0]["test"] = request.json["test"]
    component[0]["currentStateOn"] = request.json["currentStateOn"]
    component[0]["notes"] = request.json["notes"]
    component[0]["cycleOnTime"] = request.json["cycleOnTime"]
    component[0]["cycleOffTime"] = request.json["cycleOffTime"]
    component[0]["blackoutStart"] = request.json["blackoutStart"]
    component[0]["blackoutStop"] = request.json["blackoutStop"]

    # write the dictionary to json file
    jsonData = json.dumps(data, default=str)
    jsonFile = open("/home/pi/components.json", "w")
    jsonFile.write(jsonData)
    jsonFile.close()



    def loadFromJsonToObject(self):
        for i in Timer.componentsDictList:
            if (i["name"] == self.name) and (i != self.componentData):
                for k, v in i.items():
                    pass

    



















