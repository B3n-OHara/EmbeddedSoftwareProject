import RPi.GPIO as GPIO
import time
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys

ledPin = 11
PORT_NUM = 5005
SIZE = 128
mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind(('192.168.237.34', PORT_NUM))
print("listening on port {0}\n".format(PORT_NUM))


def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, GPIO.LOW)
	
def triggerLED():
	while True:
		(data,addr) = mySocket.recvfrom(SIZE)
		print(data.decode('utf-8'))
		
		if data.decode('utf-8') == '0':
			GPIO.output(ledPin, GPIO.HIGH)
			
setup()
triggerLED()
