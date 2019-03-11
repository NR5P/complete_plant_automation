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

    def loadFromJsonToObject(self):
        for i in Timer.componentsDictList:
            if (i["name"] == self.name) and (i != self.componentData):
                for k, v in i.items():
                    if v != 


    



















