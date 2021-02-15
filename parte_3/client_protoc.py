
import socket
from micro_pb2 import Microondas
teste = Microondas()
teste.temperatura = 50
PORT = 6789
HOST = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(teste.SerializeToString())
s.close()
