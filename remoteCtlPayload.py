import RPi.GPIO as GPIO
import time
from ADCDevice import *
import sys
from socket import socket, AF_INET, SOCK_DGRAM

Z_Pin = 12      # define Z_Pin
SERVER_IP = '192.168.237.34'
PORT_NUM = 5005
SIZE = 1024
print("Test client sending packets to IP {0}, via port 5000")
mySocket = socket(AF_INET, SOCK_DGRAM)
adc = ADCDevice() # Define an ADCDevice class object

def setup():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)): # Detect the ads7830
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)
    GPIO.setmode(GPIO.BOARD)        
    GPIO.setup(Z_Pin,GPIO.IN,GPIO.PUD_UP)   # set Z_Pin to pull-up mode
def loop():
    while True:     
        val_Z = GPIO.input(Z_Pin)       # read digital value of axis Z
        val_Y = adc.analogRead(0)           # read analog value of axis X and Y
        val_X = adc.analogRead(1)
        print ('value_X: %d ,\tvalue_Y: %d ,\tvalue_Z: %d'%(val_X,val_Y,val_Z))
        val_Z = str(val_Z)
        mySocket.sendto(val_Z.encode('utf-8'), (SERVER_IP,PORT_NUM))
        time.sleep(2)
        

def destroy():
    adc.close()
    GPIO.cleanup()
    
if __name__ == '__main__':
    print ('Program is starting ... ') # Program entrance
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()
        sys.exit()
