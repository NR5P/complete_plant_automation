
import RPi.GPIO as GPIO
from Timer import Timer
from webApp.app import app
import threading
from IrrigationValve import IrrigationValve
from Lights import Lights

def main():
    GPIO.setmode(GPIO.BOARD)
    threadingStart()

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
    #TODO put the list of valves and lights etc. to initiate here

def threadingStart():
    timerThread = threading.Thread(target=Timer.run())
    appThread = threading.Thread(target=app.run())

    timerThread.start()
    appThread.start()

if __name__ == "__main__":
    main()