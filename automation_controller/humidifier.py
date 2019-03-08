"""
for humidity control in greenhouse
"""

from automation_controller.Timer import Timer

import RPi.GPIO as GPIO
import pickle

class Humidifier(Timer):
    def __init__(self, pin, notes, name, on, test, currentStateOn, humidity = None):
        super().__init__(self, pin, notes, name, on, test, currentStateOn)

        self.humidity = humidity

    def run(self):
        pass