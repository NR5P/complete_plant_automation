from automation_controller.Timer import Timer
from webApp import app
import threading
from automation_controller.IrrigationValve import IrrigationValve
from automation_controller.Lights import Lights
import sys
import RPi.GPIO as GPIO
sys.path.append("/home/this/programming/complete_plant_automation/automation_controller")
sys.path.append("/home/this/programming/complete_plant_automation")

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(35, GPIO.OUT)


    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)

    threadingStart()

def threadingStart():
    timerThread = threading.Thread(target=Timer.run)
    appThread = threading.Thread(target=app.startApp)

    timerThread.start()
    appThread.start()

if __name__ == "__main__":
    main()