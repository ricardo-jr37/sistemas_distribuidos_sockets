import socket
import threading
import sys
import pickle
#clients = {}
onlines = {}
HEADER_LENGTH = 10
class Servidor():
    def __init__(self, host="localhost", port=50):

        self.clientes = []

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)

        aceptar = threading.Thread(target=self.aceptarCon)
        procesar = threading.Thread(target=self.procesarCon)

        aceptar.daemon = True
        aceptar.start()

        procesar.daemon = True
        procesar.start()

        while True:
            msg = input('->')
            if msg == 's':
                self.sock.close()
                sys.exit()
            else:
                pass


    def msg_to_all(self, msg, cliente):
        #print('to chegando aqui')
        #print(self.clientes)
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send(msg)
            except:
                self.clientes.remove(c)

    def usuarios_on(self, msg, cliente):
        try:
            cliente.send(msg)
        except:
            self.clientes.remove(c)
    
    def sair_chat(self, cliente):
        #print(onlines)
        print("{} SAIU do chat".format(str(onlines.get(cliente.getpeername()[1])[0])))
        
        teste = "Mensagem do Servidor: {} SAIU do chat".format(str(onlines.get(cliente.getpeername()[1])[0]))
        #print(teste)
        
        msg=pickle.dumps(teste)
        #print(cliente)
        #print(msg)
        onlines.pop(cliente.getpeername()[1], None)
        #print(onlines)
        self.msg_to_all(msg, cliente)
        self.clientes.remove(cliente)
        print(onlines)
        
    def aceptarCon(self):
        print("aceptarCon iniciado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
                
                #print(self.clientes)
            except:
                pass

    def procesarCon(self):
        print("ProcesarCon iniciado")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        teste = data.decode('utf-8')
                        if data:
                            teste = teste.split('/')
                            if onlines.get(c.getpeername()[1], None) == None:
                                onlines[c.getpeername()[1]] = teste
                                print('{} entrou no chat'.format(teste[0]))
                            
                            elif len(teste) > 1:
                                if teste[1] == 'USUARIOS':
                                    msg_online = 'Mensagem do Servidor!\nUsuarios onlines:\n'
                                    for key in onlines:
                                        print(onlines[key])
                                        msg_online += "{} \n".format(str(onlines[key][0]))
                                    print(msg_online)
                                    mensagem=pickle.dumps(msg_online)
                                    #msg_online = msg_online.encode('utf-8')
                                    self.usuarios_on(mensagem,c)
                                elif teste[1] == 'SAIR':
                                    self.sair_chat(c)
                                else:
                                    teste = "Mensagem do servidor: Comando invalido\n"
                                    print(teste)
                                    mensagem=pickle.dumps(teste)
                                    #print('entrando aqui 3')
                                    #self.msg_to_all(mensagem, c)
                                    c.send(mensagem)
                            else:
                                teste = data.decode('utf-8')
                                #print(teste)
                                mensagem=pickle.dumps(teste)
                                #print('entrando aqui 3')
                                self.msg_to_all(mensagem, c)
                            
                    except:
                        pass


s = Servidor()
