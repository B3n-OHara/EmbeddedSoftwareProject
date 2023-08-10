import RPi.GPIO as GPIO
import time

TPIN = 25
EPIN = 12
SPEED = 340

GPIO.setmode(GPIO.BCM)
GPIO.setup(TPIN, GPIO.OUT)
GPIO.setup(EPIN, GPIO.IN)
GPIO.output(TPIN, False)

#def sendPulse():
	#GPIO.output(TPIN, True)
	#time.sleep(0.01)
	#GPIO.output(TPIN, False)

def calcDistance():
	GPIO.output(TPIN, True)
	time.sleep(0.01)
	GPIO.output(TPIN, False)
	
	while GPIO.input(EPIN) == 0:
		timeSent = time.time()
	while GPIO.input(EPIN) == 1:
		timeRecieved = time.time()
		
	transmissionTime = timeRecieved - timeSent
	
	dist = (SPEED * transmissionTime) / 2
	print("DISTANCE FROM TARGET: ", dist, " m")
	time.sleep(1)
	if dist <= 0.2:
		boom = True
	else:
		boom = False
	
	return boom
	
def payloadTrigger():
	ledPin = 17
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, GPIO.HIGH)
	print("Payload Triggered")
					
def main():
	#sendPulse()
	if calcDistance():
		payloadTrigger()
	
try:
	while True:
		main()

except KeyboardInterrupt:
	pass
GPIO.cleanup()
