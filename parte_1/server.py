from socket import *
import socket

serverName = 'Localhost'
serverPort = 12456
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('localhost',12456))
print ('The server is connected')
while 1:

	number1, clientAddress = serverSocket.recvfrom(2048)
	print 'Number1 received:', number1

	number2, clientAddress = serverSocket.recvfrom(2048)
	print 'Number2 received:', number2
	
	number3 = int(number1.decode())*2
	number3 = str(number3)
	serverSocket.sendto(number3.encode(),clientAddress)
	number4 = int(number2.decode())*3
	number4 = str(number4)
	serverSocket.sendto(number4.encode(),clientAddress)
	
	operator, clientAddress = serverSocket.recvfrom(2048)
	print 'received operator', operator
	print 'calculating..'

if str(operator) == '+':
	answer = int(number1.decode()) + int(number2.decode())
	answer = str(answer)
	serverSocket.sendto(answer.encode(),clientAddress)
elif str(operator) == '-':
	answer = int(number1.decode()) - int(number2.decode())
	answer = str(answer)
	serverSocket.sendto(answer.encode(),clientAddress)
elif str(operator) == '/':
	answer = int(number1.decode()) / int(number2.decode())
	answer = str(answer)
	serverSocket.sendto(answer.encode(),clientAddress)
elif str(operator) == '*':
	answer = int(number1.decode()) * int(number2.decode())
	answer = str(answer)
	sererSocket.sendto(answer.encode(),clientAddress)

serverSocket.close()
