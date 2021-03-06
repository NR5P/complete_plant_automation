"""
base class for each automation component. 
"""

import json

class Timer():
    timer_list = []
    count = None # number of components currently running
    componentsDictList = []

    def __init__(self, pin, notes, name = "component {}".format(count), on = False, test = False, currentStateOn = False):
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
        """
        try:
            with open("components.json") as f:
                jsonData = json.load(f)
                if Timer.componentsDictList != jsonData:
                    Timer.componentsDictList = jsonData
                    ####TODO#### make a function to load JSON data into objects on startup and add to object list##########TODO###########33
        except NameError:
            jsonFile = open("components.json", "w")
            jsonFile.close()

    def addToJson(self, entry=None):
        """
        adds saved dictionary (componentsJson) to the json file. if a dictionary is passed and 
        the entry does not exist by the name the dictionary is updated. if the value does exist
        the entry in Timer.components with the same name is overridden
        """
        if entry:
            if Timer.isEntryAlreadyIn(entry):
                for i in Timer.componentsDictList:
                    if i["name"] == entry["name"]:
                        Timer.componentsDictList.remove(i)
                        break

            Timer.componentsDictList.append(entry)

        jsonData = json.dumps(Timer.componentsDictList, default=str)
        jsonFile = open("components.json", "w")
        jsonFile.write(jsonData)
        jsonFile.close()

    @staticmethod
    def isEntryAlreadyIn(request):
        """
        returns True if entry is already in list of dicts
        """
        try:
            with open("/home/pi/components.json", "r") as f:
                data = json.load(f)
        except:
            pass
        for i in data:
            if i["name"] == request.json["name"]:
                return True
            else:
                return False

    @staticmethod
    def run():
        """
        iterates through list once and calls run on each component
        """
        for i in Timer.timer_list:
            i.run()

    def retrieveSelfFromJson(self):
        """
        iterate through components dict list and see if there
        """
        Timer.loadJsonFile()
        for i in Timer.componentsDictList:
            if i["name"] == self.name:
                return i

    def deleteObjectFromList(self):
        objectInList = self.retrieveSelfFromJson() 
        objectInList.remove()

    










