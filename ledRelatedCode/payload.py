import RPi.GPIO as GPIO
import time

ledPin = 11

def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(ledPin, GPIO.OUT)
        GPIO.output(ledPin, GPIO.LOW)

def triggerLED():
	GPIO.output(ledPin, GPIO.HIGH)
