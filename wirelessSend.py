import sys
from socket import socket, AF_INET, SOCK_DGRAM

SERVER_IP = '192.168.237.34'
PORT_NUM = 5005
SIZE = 1024

print("Test client sending packets to IP {0}, via port 5000")

mySocket = socket(AF_INET, SOCK_DGRAM)

while True:
	message = input()
	mySocket.sendto(message.encode('utf-8'), (SERVER_IP,PORT_NUM))

sys.exit()
