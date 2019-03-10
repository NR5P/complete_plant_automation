"""
to control heater in greenhouse
"""

from automation_controller.Timer import Timer

import RPi.GPIO as GPIO

class Heater(Timer):
    def __init__(self, pin, notes, name, on, test, currentStateOn, temperature = None):
        super().__init__(self, pin, notes, name, on, test, currentStateOn)

        self.temperature = temperature

    def run(self):
        pass