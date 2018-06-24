import Timer
import datetime
import RPi.GPIO as GPIO
import time


class IrrigationValve(Timer):
    def __init__(self, pin, name):
        super().__init__(pin, name)

        self.cycleOrIrrigate = None
        self.irrigationTimes = {}
        self.cycleOnTime = None
        self.cycleOffTime = None
        self.blackoutStart = None
        self.blackoutStop = None
        self.days = set()

    def run(self):
        def runLoop():
            cycleOn = datetime.datetime.now() + self.cycleOnTime
            time.sleep(.1)
            while True:
                if self.onOff == "off" or self.cycleOrIrrigate == "irrigate":
                    GPIO.output(self.pin, False)
                    break
                elif datetime.datetime.now() > cycleOn:
                    cyclePause = datetime.datetime.now() + self.cycleOffTime
                    while True:
                        time.sleep(.1)
                        if self.onOff == "off" or self.cycleOrIrrigate == "irrigate":
                            GPIO.output(self.pin, False)
                            break
                        elif datetime.datetime.now() > cyclePause:
                            GPIO.output(self.pin, False)
                            runLoop()
                        elif datetime.datetime.now() < cyclePause:
                            GPIO.output(self.pin, False)
                elif datetime.datetime.now() < cycleOn:
                    GPIO.output(self.pin, True)

        while True:
            time.sleep(.1)
            if self.test == "on":
                GPIO.output(self.pin, True)
            if self.onOff == "on":
                if self.cycleOrIrrigate == "irrigate":
                    for key, value in self.irrigationTime.items():
                        combinedTime = datetime.datetime.combine(datetime.date.today(), key)
                        if datetime.datetime.now() > combinedTime and datetime.datetime.now() < combinedTime + value:
                            GPIO.output(self.pin, True)
                        else:
                            GPIO.output(self.pin, False)
                elif self.cycleOrIrrigate == "cycle":
                    if self.blackoutStart != None and self.blackoutStop != None:
                        combinedTimeStart = datetime.datetime.combine(datetime.date.today(), self.blackoutStart)
                        combinedTimeStop = datetime.datetime.combine(datetime.date.today(), self.blackoutStop)
                        if datetime.datetime.now() < combinedTimeStart and datetime.datetime.now() > combinedTimeStop:
                            runLoop()
                    else:
                        runLoop()
            else:
                if self.onOff == "off":
                    GPIO.output(self.pin, False)


