import RPi.GPIO as GPIO
import time

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
	
	while True:
		angle = float(input("Enter Angle Between 0 & 180: "))
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
	
