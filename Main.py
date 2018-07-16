
import RPi.GPIO as GPIO
from Timer import Timer
from webApp.app import app
import threading

def main():
    GPIO.setmode(GPIO.BOARD)
    threadingStart()


def threadingStart():
    timerThread = threading.Thread(target=Timer.run())
    appThread = threading.Thread(target=app.run())

    timerThread.start()
    appThread.start()

if __name__ == "__main__":
    main()