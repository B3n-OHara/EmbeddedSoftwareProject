import RPi.GPIO as GPIO
import time

ledPin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, GPIO.LOW)

def loop():
	while True:
		GPIO.output(ledPin, GPIO.HIGH)
		print('LED ON')
		time.sleep(1)
		GPIO.output(ledPin, GPIO.LOW)
		print('LED OFF')
		time.sleep(1)

def main():
	setup()
	loop()

if __name__ == '__main__':
	main()
