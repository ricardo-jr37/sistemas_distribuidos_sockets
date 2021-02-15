
import socket
from micro_pb2 import Microondas

HOST = 'localhost'
PORT = 6789
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
micro = Microondas()
conn, addr = s.accept()
data = conn.recv(4096)
print(data)
micro.ParseFromString(data)
print(micro.temperatura)
#conn.sendall(data_string)
conn.close()
