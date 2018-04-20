
import datetime
import time
import RPi.GPIO as GPIO
import threading
import pickle


class Valve():
    valveList = []

    def __init__(self, pin, name):
        self.name = name
        self.onOff = "off"
        self.test = "off"
        self.pin = pin
        self.cycleOrIrrigate = None
        self.currentState = "off"
        self.irrigationTime = {}
        self.cycleOnTime = None
        self.cycleOffTime = None
        self.blackoutStart = None
        self.blackoutStop = None
        self.days = set()
        self.threadStart()

        try:
            file = open(self.name, "rb")
            self = pickle.load(file)
            file.close
            Valve.valveList.append(self)
        except:
            self.saveValve()
            Valve.valveList.append(self)
        
    def __str__(self):
        return self.name

    def saveValve(self):
        file = open(self.name, "wb")
        pickle.dump(self, file)
        file.close()

    def threadStart(self):
        t = threading.Thread(target=self.run)
        t.start()
        
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




                    
                    
    
    


    












































