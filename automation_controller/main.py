"""
homestead automation timer for growing plants. has capabilities for both normal gardent/farming irrigation as
as well as ability to intermently mist plants for propagation. has capabilities for climate control in 
greenhouse and the use of sensors including humidity and temperature. 
"""

from .Timer import Timer

import RPi.GPIO as GPIO

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

    timer = Timer
    timer.loadJsonFile()

    timer.run()
    

if __name__ == "__main__":
    main()