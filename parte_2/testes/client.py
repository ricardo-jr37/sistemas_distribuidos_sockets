import socket
import threading

class Client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name = input('informe seu nome: ')
    
    def sendMsg(self):
        while True:
            self.s.send(bytes(input(f'{self.name} > '), 'utf-8'))
    
    def __init__(self):
        self.s.connect(('localhost', 1234))
        
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        
        while True:
            data = self.s.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))

Client()
