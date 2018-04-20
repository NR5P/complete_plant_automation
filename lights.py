import datetime
import time
import RPi.GPIO as GPIO
import threading
import pickle

class Lights():
    lights_list = []

    def __init__(self, pin, name):
        self.name = name
        self.onOff = "off"
        self.test = "off"
        self.pin = pin
        self.current_state = "off"
        self.time_on = None
        self.time_off = None
        self.threadStart()

        try:
            file = open(self.name, "rb")
            self = pickle.load(file)
            file.close
            Lights.lights_list.append(self)
        except:
            self.saveLights()
            Lights.lights_list.append(self)

    def __str__(self):
        return self.name

    def saveLights(self):
        file = open(self.name, "wb")
        pickle.dump(self, file)
        file.close()

    def threadStart(self):
        t = threading.Thread(target=self.run)
        t.start()

    def run(self):
        while True:
            time.sleep(.1)
            if self.test == "on":
                GPIO.output(self.pin, True)
            if self.onOff == "on":
                if self.time_on != None and self.time_off != None:
                    now = datetime.datetime.now()
                    on_time_today = now.replace(self.time_on) 
                    off_time_today = now.replace(self.time_off) 
                    if now > on_time_today and now < off_time_today:
                        self.onOff = "on"
                    else:
                        self.onOff = "off"
