import Timer
import datetime
import time
import RPi.GPIO as GPIO


class Lights(Timer):
    def __init__(self, pin, name):
        super().__init__(pin, name)
        self.time_on = None
        self.time_off = None

    def run(self):
        while True:
            time.sleep(.1)
            if self.test == "on":
                GPIO.output(self.pin, True)
            if self.onOff == "on":
                if self.time_on is not None and self.time_off is not None:
                    now = datetime.datetime.now()
                    on_time_today = now.replace(self.time_on)
                    off_time_today = now.replace(self.time_off)
                    if now > on_time_today and now < off_time_today:
                        self.on = False
                    else:
                        self.on = False