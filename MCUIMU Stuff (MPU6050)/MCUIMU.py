import sys
import time
import math
import RPi.GPIO as GPIO
import Adafruit_DHT
import MPU6050


	
def dht():

	humidity, temperature = Adafruit_DHT.read_retry(11, 22)
	print(' Temp: {0:0.1f} C	Humidity; {1:0.1f} %'.format(temperature, humidity))

def MpU():
	
	mpu = MPU6050.MPU6050(1, 0x68)
	
	#temp please remove
	accel = [0.0]*3
	accError = [0]*3
	
	accel = mpu.get_acceleration()
	gyro = mpu.get_rotation()
	print("Acc ", accel)
	print("Rotation ", gyro)
	
	print
	
	def setup():
		mpu.dmp_initialize()
		calculate_acc_error()
	
	def calculate_acc_error():
		global accError, GyroError
		
		accel = [0.0]*3
		
		i=0
		while(i<200):
			accel = mpu.get_acceleration()
			
			accel[0] /= 16384.0
			accel[1] /= 16384.0
			accel[2] /= 16384.0
		
			accError[0] += ((math.atan((accel[1]) / math.sqrt(math.pow(accel[0],2) + math.pow(accel[2],2))) * 180 / math.pi))
			accError[1] += ((math.atan(-1*(accel[0]) / math.sqrt(math.pow(accel[1],2) + math.pow(accel[2],2))) * 180 / math.pi))
			i+=1
		
		accError[0] /= 200
		accError[1] /= 200
		
		print("Acc Error: ", accError)
		
		return
	
	def loop():
		global accError
		
		accel = [0.0]*3
		gyro = [0.0]*3
		
		while True:
			accel = mpu.get_acceleration()
			gyro = mpu.get_rotation()
			
			accel[0] /= 16384.0
			accel[1] /= 16384.0
			accel[2] /= 16384.0
			
			accAngleX = (math.atan(accel[1] / math.sqrt(math.pow(accel[0],2) + math.pow(accel[2],2))) * 180 / math.pi) - accError[0]
			accAngleY = ((math.atan(-1*(accel[0]) / math.sqrt(math.pow(accel[1],2) + math.pow(accel[2],2))) * 180 / math.pi)) - accError[1]
			
			print("Roll: ", accAngleX, ", Pitch: ", accAngleY)
			
			time.sleep(0.1) 
	
	#setup()
	calculate_acc_error()
	#loop()

def main():

	#dht()
	#while True:
	MpU()
	#time.sleep(2)

if __name__ == '__main__':
	main()
