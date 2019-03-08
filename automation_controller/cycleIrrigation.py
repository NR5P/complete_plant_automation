"""
for cycle irrigation like for propagating plants. takes on time, off time, and a blackout time. typically 
for short bursts of irrigation
"""

from automation_controller.Timer import Timer

import time
import datetime
import pickle
import RPi.GPIO as GPIO

class CycleIrrigation(Timer):
    def __init__(self):

        self.cycleOnTime = None
        self.cycleOffTime = None
        self.blackoutStart = None
        self.blackoutStop = None

    def run(self):
        pass