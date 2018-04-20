from irrigationTimer import Valve
from timer_socket import socket_connection
import RPi.GPIO as GPIO

valve1Pin = 8
valve2Pin = 10
valve3Pin = 12
valve4Pin = 16
valve5Pin = 18
valve6Pin = 22
valve7Pin = 24
valve8Pin = 26
valve9Pin = 32
valve10Pin = 36

# sets to board pin number scheme
GPIO.setmode(GPIO.BOARD)

# setup valve pins as outputs
GPIO.setup(valve1Pin, GPIO.OUT)
GPIO.setup(valve2Pin, GPIO.OUT)
GPIO.setup(valve3Pin, GPIO.OUT)
GPIO.setup(valve4Pin, GPIO.OUT)
GPIO.setup(valve5Pin, GPIO.OUT)
GPIO.setup(valve6Pin, GPIO.OUT)
GPIO.setup(valve7Pin, GPIO.OUT)
GPIO.setup(valve8Pin, GPIO.OUT)
GPIO.setup(valve9Pin, GPIO.OUT)
GPIO.setup(valve10Pin, GPIO.OUT)

#set all valve pins to off
GPIO.output(valve1Pin, False)
GPIO.output(valve2Pin, False)
GPIO.output(valve3Pin, False)
GPIO.output(valve4Pin, False)
GPIO.output(valve5Pin, False)
GPIO.output(valve6Pin, False)
GPIO.output(valve7Pin, False)
GPIO.output(valve8Pin, False)
GPIO.output(valve9Pin, False)
GPIO.output(valve10Pin, False)


def main():
    valve1 = Valve(valve1Pin, "valve 1")
    valve2 = Valve(valve2Pin, "valve 2")
    valve3 = Valve(valve3Pin, "valve 3")
    valve4 = Valve(valve4Pin, "valve 4")
    valve5 = Valve(valve5Pin, "valve 5")
    valve6 = Valve(valve6Pin, "valve 6")
    valve7 = Valve(valve7Pin, "valve 7")
    valve8 = Valve(valve8Pin, "valve 8")
    valve9 = Valve(valve9Pin, "valve 9")
    valve10 = Valve(valve10Pin, "valve 10")

    socket_connection()



if __name__ == "__main__":
    main()
