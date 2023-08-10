import RPi.GPIO as GPIO
import time
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys

PORT_NUM = 5005
SIZE = 128
SPIN = 18
#OFFSE_DUTY = 0.5
#SERVO_MIN_DUTY = 2.5 + OFFSE_DUTY
#SERVO_MAX_DUTY = 12.5 + OFFSE_DUTY

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(SPIN, GPIO.OUT)
	GPIO.output(SPIN, GPIO.LOW)
	
def calcDutyCycle(angle):
	calc = angle / 18 + 2
	return calc
	
def main():
	setup()
	pwm = GPIO.PWM(SPIN, 50)
	pwm.start(0)
	mySocket = socket(AF_INET, SOCK_DGRAM)
	mySocket.bind(('192.168.237.34', PORT_NUM))

	print("listening on port {0}\n".format(PORT_NUM))
	
	while True:
		(data,addr) = mySocket.recvfrom(SIZE)
		print(data.decode('utf-8'))
		angle = float(data)
		GPIO.output(SPIN, True)
		pwm.ChangeDutyCycle(calcDutyCycle(angle))
		time.sleep(1)
		GPIO.output(SPIN, False)
		pwm.ChangeDutyCycle(calcDutyCycle(angle))
try:
	main()

except KeyboardInterrupt:
	pass
pwm.stop()
GPIO.cleanup()
sys.exit()
	
