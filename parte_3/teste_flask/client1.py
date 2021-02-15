#temperatura_quarto
# C:\projetos\git\sistemas_distribuidos_sockets\parte_3\teste_flask
import time
import socket
from sensores_pb2 import Sensor
import random

import pdb
#pdb.set_trace()
PORT = 1510
HOST = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    
    ruido = random.random()
    fator = random.randrange(-1, 2, 1)
    final = ruido*fator
    sensor = Sensor()
    #pdb.set_trace()
    sensor.nome='cozinha'
    sensor.temperatura_cozinha = 40 + final
    print(sensor.nome)
    print(sensor.temperatura_cozinha)
    s.sendall(sensor.SerializeToString())
    #print('mensagem enviada')
    time.sleep(10)
    
s.close()