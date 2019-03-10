"""
base class for each automation component. 
"""

import json

class Timer():
    timer_list = []
    count = None # number of components currently running
    componentsDictList = []

    def __init__(self, pin, notes, name = f"component {count}", on = False, test = False, currentStateOn = False):
        self.name = name
        self.pin = pin
        self.on = on
        self.test = test
        self.currentStateOn = currentStateOn
        self.notes = notes

    def __str__(self):
        return self.name

    @staticmethod
    def loadJsonFile():
        """
        checks if there is a json file already open. if there is not a file it creates one
        then it returns the dictionary.
        """
        try:
            with open("components.json") as f:
                jsonData = json.load(f)
                #return jsonData
                Timer.componentsDictList = jsonData
        except NameError:
            jsonFile = open("components.json", "w")
            jsonFile.close()

    def addToJson(self, data=None):
        """
        adds saved dictionary (componentsJson) to the json file. if a dictionary is passed and 
        the entry does not exist by the name the dictionary is updated. if the value does exist
        the entry in Timer.components with the same name is overridden
        """
        if data:
            if self.isEntryAlreadyIn(data):
                for i in Timer.componentsDictList:
                    if i["name"] == data["name"]:
                        Timer.componentsDictList.remove(i)
                        break
            else:
                Timer.componentsDictList.append(data)

        jsonData = json.dumps(Timer.componentsDictList, default=str)
        jsonFile = open("components.json", "w")
        jsonFile.write(jsonData)
        jsonFile.close()

    def isEntryAlreadyIn(self, entry):
        """
        returns True if entry is already in list of dicts
        """
        for i in Timer.componentsDictList:
            if i["name"] == entry["name"]:
                return True
            else:
                return False

    @staticmethod
    def run():
        while True:
            for i in Timer.timer_list:
                i.run()










