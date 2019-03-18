"""
to control fan
"""

from automation_controller.Timer import Timer

import RPi.GPIO as GPIO
import json

class Fan(Timer):
    def __init__(self, pin, notes, name, on, test, currentStateOn, temperature = None):
        super().__init__(self, pin, notes, name, on, test, currentStateOn)

        self.temperature = temperature
        #TODO add temperature variations, ex(ontime and offtime)


    @staticmethod
    def addToJson(request):
        try:
            with open("/home/pi/components.json", "r") as f:
                data = json.load(f) # load the json file into a dictionary
        except:
            print("issue opening file")
        componentData = {
            "type" : request.json["type"],
            "name" : request.json["name"],
            "pin" : request.json["pin"],
            "on" : request.json["on"],
            "test" : request.json["test"],
            "currentStateOn" : request.json["currentStateOn"],
            "notes" : request.json["notes"],
            "temperature" : request.json["temperature"]
        }
        # append to dictionary of json data
        data.append(componentData)

        # write the dictionary to json file
        jsonData = json.dumps(data)
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
        component[0]["temperature"] = request.json["temperature"]

        # write the dictionary to json file
        jsonData = json.dumps(data)
        jsonFile = open("/home/pi/components.json", "w")
        jsonFile.write(jsonData)
        jsonFile.close()



        

    def run(self):
        pass
    















