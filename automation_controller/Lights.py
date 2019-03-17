from automation_controller.Timer import Timer
import datetime
import time

import RPi.GPIO as GPIO
import json


class Lights(Timer):

    def __init__(self, pin, notes, name, on, test, currentStateOn, time_on = None, time_off = None):
        super().__init__(self, pin, notes, name, on, test, currentStateOn)
        self.time_on = time_on
        self.time_off = time_off
        Timer.timer_list.append(self)

        try:
            self.load()
        except:
            self.save()

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
                "timeOn" : request.json["timeOn"],
                "timeOff" : request.json["timeOff"]
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
        component[0]["timeOn"] = request.json["timeOn"]
        component[0]["timeOff"] = request.json["timeOff"]

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
            if self.time_on is not None and self.time_off is not None:
                now = datetime.datetime.now()
                on_time_today = now.replace(self.time_on)
                off_time_today = now.replace(self.time_off)
                if now > on_time_today and now < off_time_today:
                    self.on = True
                else:
                    self.on = False
        else:
            GPIO.output(self.pin, False)