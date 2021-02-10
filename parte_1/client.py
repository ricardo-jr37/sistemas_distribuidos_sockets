
from socket import * 
import socket

serverName = 'Localhost'
serverport = 12456
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print 'Traget IP: ', serverName
print 'Target Port:', serverport
print '\n'


number1 = raw_input ('Input number1: ')
number2 = raw_input ('Input number2: ')
operator = raw_input ('Select an operator: (+ / * -) ')



clientSocket.sendto(number1.encode(),(serverName,serverport))
clientSocket.sendto(number2.encode(),(serverName,serverport))
clientSocket.sendto(operator.encode(),(serverName,serverport))


number3,serverAddress = clientSocket.recvfrom(2048)
print 'Sent back number 3: ', number3
number4,serverAddress = clientSocket.recvfrom(2048)
print 'Number4  send back: ', number4
answer,serverAddress = clientSocket.recvfrom(2048)
print 'your result: ', answer

clientSocket.close()

