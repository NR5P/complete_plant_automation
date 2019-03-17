"""
for timed irrigation for typical garden irrigation. 
"""

from automation_controller.Timer import Timer

import datetime
import RPi.GPIO as GPIO
import time
import json


class IrrigationValve(Timer):

    def __init__(self, pin, notes, name, on, test, currentStateOn, irrigationTimes = {}, days = set()):
        super().__init__(self, pin, notes, name, on, test, currentStateOn)

        self.irrigationTimes = irrigationTimes
        self.days = days 
        Timer.timer_list.append(self)

        try:
            self.load()
        except:
            self.save()

    def __str__(self):
        return self.name

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
                "irrigationTimes" : request.json["irrigationTimes"]
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

        component[0]["componentType"] = request.json["type"]
        component[0]["name"] = request.json["name"]
        component[0]["pin"] = request.json["pin"]
        component[0]["on"] = request.json["on"]
        component[0]["test"] = request.json["test"]
        component[0]["currentStateOn"] = request.json["currentStateOn"]
        component[0]["notes"] = request.json["notes"]
        component[0]["irrigationTimes"] = request.json["irrigationTimes"]

        # write the dictionary to json file
        jsonData = json.dumps(data, default=str)
        jsonFile = open("/home/pi/components.json", "w")
        jsonFile.write(jsonData)
        jsonFile.close()


    

    def run(self):
        time.sleep(.1)
        if self.test:
            GPIO.output(self.pin, True)
        if self.on:
            if self.cycleOrIrrigate == "irrigate":
                for key, value in self.irrigationTime.items():
                    combinedTime = datetime.datetime.combine(datetime.date.today(), key)
                    if datetime.datetime.now() > combinedTime and datetime.datetime.now() < combinedTime + value:
                        GPIO.output(self.pin, True)
                    else:
                        GPIO.output(self.pin, False)
            elif self.cycleOrIrrigate == "cycle":
                if self.blackoutStart is not None and self.blackoutStop is None:
                    combinedTimeStart = datetime.datetime.combine(datetime.date.today(), self.blackoutStart)
                    combinedTimeStop = datetime.datetime.combine(datetime.date.today(), self.blackoutStop)
                    if combinedTimeStart > datetime.datetime.now() > combinedTimeStop:
                        GPIO.output(self.pin, True)
                else:
                    GPIO.output(self.pin, False)
        else:
                GPIO.output(self.pin, False)






