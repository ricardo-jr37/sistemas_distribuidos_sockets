"""
import socket
from sensores_pb2 import Sensor

HOST = 'localhost'
PORT = 1010
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
while True:
	conn, addr = s.accept()
	data = conn.recv(4096)
	micro = Sensor()
	micro.ParseFromString(data)
	print(micro.nome)
#conn.sendall(data_string)
conn.close()
"""
import pdb
#pdb.set_trace()
import sys
import threading
import socket
from sensores_pb2 import Sensor
class Servidor():
    status=0
    tmpcozinha = 0
    tmpquarto = 0
    def __init__(self, host="localhost", port=1510):

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
    
    def aceptarCon(self):
        print("aceptarCon iniciado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
                conn.send(('HTTP/1.0 200 OK\n').encode('utf-8'))
                conn.send(('Content-Type: text/html\n').encode('utf-8'))
                conn.send(('\n').encode('utf-8')) # header and body should be separated by additional newline
                conn.send(("""
                    <html>
                        <body>
                            <h1>Trabalho Sistemas Distribuidos!</h1>
                            <h3>Temperatura cozinha: </h3>
                """).encode('utf-8'))
                mensagem = "<h4>{} graus Celsius</h4>".format(self.tmpcozinha)
                conn.send(mensagem.encode('utf-8'))
                mensagem2 = "<h3>Temperatura quarto: </h3><h4>{} graus Celsius</h4>".format(self.tmpquarto)
                conn.send(mensagem2.encode('utf-8'))
                mensagem3 = "<h3>Status da lampada: </h3><h4>{}</h4>".format(self.status)
                conn.send(mensagem3.encode('utf-8'))
                conn.send(("""
                        </body>
                    </html>
                """).encode('utf-8')) # Use triple-quote string.
            except:
                pass
    def procesarCon(self):
        print("ProcesarCon iniciado")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        if data:
                            #print(data)
                            sensor = Sensor()
                            sensor.ParseFromString(data)
                            print(sensor.nome)
                            if sensor.nome=='quarto':
                                self.tmpquarto = sensor.temperatura_quarto
                                #print('Temperatura do quarto: ',sensor.temperatura_quarto, ' graus Celsius')
                                conn.send(("""
                                    <html>
                                        <body>
                                            <h1>Trabalho Sistemas Distribuidos!</h1>
                                            <h3>Temperatura cozinha: </h3>
                                """).encode('utf-8'))
                                mensagem = "<h4>{} graus Celsius</h4>".format(self.tmpcozinha)
                                conn.send(mensagem.encode('utf-8'))
                                mensagem2 = "<h3>Temperatura quarto: </h3><h4>{} graus Celsius</h4>".format(self.tmpquarto)
                                conn.send(mensagem2.encode('utf-8'))
                                mensagem3 = "<h3>Status da lampada: </h3><h4>{}</h4>".format(self.status)
                                conn.send(mensagem3.encode('utf-8'))
                                conn.send(("""
                                        </body>
                                    </html>
                                """).encode('utf-8')) # Use triple-quote string.
                            elif sensor.nome=='cozinha':
                            	#print(sensor.temperatura_cozinha)
                                self.tmpcozinha = sensor.temperatura_cozinha
                                print('Temperatura do quarto: ',sensor.temperatura_quarto, ' graus Celsius')
                                conn.send(("""
                                    <html>
                                        <body>
                                            <h1>Trabalho Sistemas Distribuidos!</h1>
                                            <h3>Temperatura cozinha: </h3>
                                """).encode('utf-8'))
                                mensagem = "<h4>{} graus Celsius</h4>".format(self.tmpcozinha)
                                conn.send(mensagem.encode('utf-8'))
                                mensagem2 = "<h3>Temperatura quarto: </h3><h4>{} graus Celsius</h4>".format(self.tmpquarto)
                                conn.send(mensagem2.encode('utf-8'))
                                mensagem3 = "<h3>Status da lampada: </h3><h4>{}</h4>".format(self.status)
                                conn.send(mensagem3.encode('utf-8'))
                                conn.send(("""
                                        </body>
                                    </html>
                                """).encode('utf-8')) # Use triple-quote string.
                                #print('Temperatura da cozinha: ',sensor.temperatura_cozinha, ' graus Celsius')
                            else:
                                status = sensor.status_lampada
                                if sensor.status_lampada == 1:
                                	self.status = 1
                                	conn.send(("""
                                    <html>
                                        <body>
                                            <h1>Trabalho Sistemas Distribuidos!</h1>
                                            <h3>Temperatura cozinha: </h3>
	                                """).encode('utf-8'))
	                                mensagem = "<h4>{} graus Celsius</h4>".format(self.tmpcozinha)
	                                conn.send(mensagem.encode('utf-8'))
	                                mensagem2 = "<h3>Temperatura quarto: </h3><h4>{} graus Celsius</h4>".format(self.tmpquarto)
	                                conn.send(mensagem2.encode('utf-8'))
	                                mensagem3 = "<h3>Status da lampada: </h3><h4>{}</h4>".format(self.status)
	                                conn.send(mensagem3.encode('utf-8'))
	                                conn.send(("""
	                                        </body>
	                                    </html>
	                                """).encode('utf-8')) 
                                    #print('Status da lampada: Ligada')
                                else:
                                	self.status = 0
                                	conn.send(("""
                                    <html>
                                        <body>
                                            <h1>Trabalho Sistemas Distribuidos!</h1>
                                            <h3>Temperatura cozinha: </h3>
	                                """).encode('utf-8'))
	                                mensagem = "<h4>{} graus Celsius</h4>".format(self.tmpcozinha)
	                                conn.send(mensagem.encode('utf-8'))
	                                mensagem2 = "<h3>Temperatura quarto: </h3><h4>{} graus Celsius</h4>".format(self.tmpquarto)
	                                conn.send(mensagem2.encode('utf-8'))
	                                mensagem3 = "<h3>Status da lampada: </h3><h4>{}</h4>".format(self.status)
	                                conn.send(mensagem3.encode('utf-8'))
	                                conn.send(("""
	                                        </body>
	                                    </html>
	                                """).encode('utf-8')) 
                            #print(data.decode('utf-8'))
                            #self.msg_to_all(data,c)
                    except:
                        pass


s = Servidor()