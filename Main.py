from automation_controller.Timer import Timer
from webApp.app import app
import threading
from automation_controller.IrrigationValve import IrrigationValve
from automation_controller.Lights import Lights
import RPi.GPIO as GPIO
import sys
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


    valve_1 = IrrigationValve(11, "valve 1")
    valve_2 = IrrigationValve(13, "valve 2")
    valve_2 = IrrigationValve(15, "valve 3")
    valve_2 = IrrigationValve(19, "valve 4")
    valve_2 = IrrigationValve(21, "valve 5")
    valve_2 = IrrigationValve(23, "valve 6")
    valve_2 = IrrigationValve(29, "valve 7")
    valve_2 = IrrigationValve(31, "valve 8")
    valve_2 = IrrigationValve(33, "valve 9")
    valve_2 = IrrigationValve(35, "valve 10")

    lights_1 = Lights(37, "lights 1")
    lights_2 = Lights(8, "lights 2")

    threadingStart()

def threadingStart():
    timerThread = threading.Thread(target=Timer.run())
    appThread = threading.Thread(target=app.run())

    timerThread.start()
    appThread.start()

if __name__ == "__main__":
    main()