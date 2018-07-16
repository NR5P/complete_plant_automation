
import RPi.GPIO as GPIO
from Timer import Timer

def main():
    GPIO.setmode(GPIO.BOARD)

    Timer.run()


if __name__ == "__main__":
    main()