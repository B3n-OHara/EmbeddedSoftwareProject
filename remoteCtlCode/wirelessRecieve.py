from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys

PORT_NUM = 5005
SIZE = 128

#hostName = gethostbyname('192.168.237.185')

mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind(('192.168.237.34', PORT_NUM))

print("listening on port {0}\n".format(PORT_NUM))

while True:
	(data,addr) = mySocket.recvfrom(SIZE)
	print(data.decode('utf-8'))

sys.exit()
