from automation_controller.Timer import Timer
import datetime
import RPi.GPIO as GPIO
import time
import pickle


class IrrigationValve(Timer):
    valveList = []

    test = "some testing text"
    idNumber = 0

    def __init__(self, pin, name):
        super().__init__(pin, name)

        IrrigationValve.idNumber += 1
        self.id = IrrigationValve.idNumber
        self.name = name
        self.notes = None
        self.on = False
        self.cycleOrIrrigate = None
        self.irrigationTimes = {}
        self.cycleOnTime = None
        self.cycleOffTime = None
        self.blackoutStart = None
        self.blackoutStop = None
        self.days = set()
        Timer.timer_list.append(self)
        IrrigationValve.valveList.append(self)


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






