"""
for timed irrigation for typical garden irrigation. 
"""

from automation_controller.Timer import Timer

import datetime
import RPi.GPIO as GPIO
import time
import pickle


class IrrigationValve(Timer):

    def __init__(self, pin, notes, name, on, test, currentStateOn, irrigationTimes = {}, days = set()):
        super().__init__(self, pin, notes, name, on, test, currentStateOn)

        self.irrigationTimes = irrigationTimes
        self.days = days 
        Timer.timer_list.append(self)

        try:
            self.load()
        except:
            self.save()

    def __str__(self):
        return self.name

    def run(self):
        time.sleep(.1)
        if self.test:
            GPIO.output(self.pin, True)
        if self.on:
            if self.cycleOrIrrigate == "irrigate":
                for key, value in self.irrigationTime.items():
                    combinedTime = datetime.datetime.combine(datetime.date.today(), key)
                    if datetime.datetime.now() > combinedTime and datetime.datetime.now() < combinedTime + value:
                        GPIO.output(self.pin, True)
                    else:
                        GPIO.output(self.pin, False)
            elif self.cycleOrIrrigate == "cycle":
                if self.blackoutStart is not None and self.blackoutStop is None:
                    combinedTimeStart = datetime.datetime.combine(datetime.date.today(), self.blackoutStart)
                    combinedTimeStop = datetime.datetime.combine(datetime.date.today(), self.blackoutStop)
                    if combinedTimeStart > datetime.datetime.now() > combinedTimeStop:
                        GPIO.output(self.pin, True)
                else:
                    GPIO.output(self.pin, False)
        else:
                GPIO.output(self.pin, False)






