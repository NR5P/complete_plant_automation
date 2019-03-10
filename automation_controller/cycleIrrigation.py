"""
for cycle irrigation like for propagating plants. takes on time, off time, and a blackout time. typically 
for short bursts of irrigation
"""

from automation_controller.Timer import Timer

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

    def run(self):
        pass
    
    def save(self):
        componentData = {"type" : "cycle",
                         "name" : self.name,
                         "pin"  : self.pin,
                         "on"   : self.on,
                         "currentlyOn" : self.currentStateOn,
                         "test" : self.test,
                         "notes": self.notes,
                         "blackoutStart" : self.blackoutStart,
                         "blackoutStop" : self.blackoutStop}
        self.addToJson(componentData)

    def retrieveSelfFromJson(self):
        """
        iterate through components dict list and see if 
        """
        Timer.loadJsonFile()
        for i in Timer.componentsDictList:
            if i["name"] == self.name:
                return i





















