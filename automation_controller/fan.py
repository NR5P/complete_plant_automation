"""
to control fan
"""

from automation_controller.Timer import Timer

import RPi.GPIO as GPIO

class Fan(Timer):
    def __init__(self, pin, notes, name, on, test, currentStateOn, temperature = None):
        super().__init__(self, pin, notes, name, on, test, currentStateOn)

        self.temperature = temperature
        #TODO add temperature variations, ex(ontime and offtime)

    def run(self):
        pass