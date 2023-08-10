import RPi.GPIO as GPIO
import time

latchPin = 20
clkPin = 24
dataPin = 21

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(latchPin, GPIO.OUT)
	GPIO.setup(clkPin, GPIO.OUT)
	GPIO.setup(dataPin, GPIO.OUT)
	
	GPIO.output(latchPin, GPIO.LOW)
	GPIO.output(clkPin, GPIO.LOW)
	print("setup")
	
def pulseClk():
	GPIO.output(clkPin, GPIO.HIGH)
	time.sleep(0.01)
	GPIO.output(clkPin, GPIO.LOW)
	print("Clock Pulsed")
	return

def serLatch():
	GPIO.output(latchPin, GPIO.HIGH)
	time.sleep(0.01)
	GPIO.output(latchPin, GPIO.LOW)
	print("Latch Pulsed")
	return

def regWrite(value):
	for i in range(0, 8):
		temp = value & 0x80
		if temp == 0x80:
			GPIO.output(dataPin, GPIO.HIGH)
			print("High")
		else:
			GPIO.output(dataPin, GPIO.LOW)
			print("Low")
		time.sleep(0.2)
		pulseClk()
		value = value << 0x01
	serLatch()
	return

def convBin(value):
	binVal = '0b'
	for i in range(0, 8):
		temp = value & 0x80
		if temp == 0x80:
			binVal += '1'
			print("binVal added 1")
		else:
			binVal += '0'
			print("binval added 0")
		time.sleep(0.2)
		value = value << 1
	return binVal

setup()
temp = 1
for i in range(0, 8):
	regWrite(temp)
	temp = temp << 1
	print("reg wrote left")
	
for j in range(0, 8):
	temp = temp >> 1
	regWrite(temp)
	print("reg wrote right")
