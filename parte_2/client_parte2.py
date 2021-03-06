import socket
import threading
import sys
import pickle
HEADER_LENGTH = 10
entrar = input('Seja bem-vindo:\nSe quiser entrar no chat use o comando: /ENTRAR\n')
while entrar != '/ENTRAR':
    print('Comando invalido. Tente novamente!')
    entrar = input('Se quiser entrar no chat use o comando: /ENTRAR\n')

print('Vamos se conectar no servidor, agora!\n')
x = 0
ips = input('Digite o ip do servidor: ')
ports = input('Digite a porta do servidor: ')

if (ips == 'localhost' or ips == '127.0.0.1') and int(ports) == 50:
    x = 1

while x==0:
    print('Servidor não encontrado. Tente novamente!')
    ips = input('Digite o ip do servidor: ')
    ports = input('Digite a porta do servidor: ')
    if (ips == 'localhost' or ips == '127.0.0.1') and int(ports) == 50:
        x = 1
print('Conectado ao Servidor!')
class Cliente():
    my_username = input('Informe seu nick: ')
    
    def __init__(self, host='localhost', port=50):
    
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((str(host), int(port)))
        username = self.my_username.encode('utf-8')
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
        #s.sendall(bytes(message_header + message, 'utf-8'))
        self.s.send(username)
        #self.s.send(pickle.dumps(username))
        
        msg_recv = threading.Thread(target=self.msg_recv)
        
        
        
        msg_recv.deamno = True
        msg_recv.start()
        aux = 0
        while True:
            msg = input('')
            if aux == 1:
                break
            if msg:
                if msg == '/SAIR':
                    msg = '{}: {}'.format(self.my_username, msg)
                    self.send_msg(msg)
                    aux = 1
                else:              
                    msg = '{}: {}'.format(self.my_username, msg)
                    self.send_msg(msg)
        
        self.s.close()            
        print('ATÉ MAIS!')
    def msg_recv(self):
        while True:
            try:
                data=self.s.recv(1024)
                if data:
                    print(pickle.loads(data))
            except:
                pass
    
    def send_msg(self, msg):
        self.s.send(msg.encode('utf-8'))
    
    
c = Cliente()
