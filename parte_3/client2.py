import time
import socket
from sensores_pb2 import Sensor
import random


PORT = 1510
HOST = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    ruido = random.random()
    fator = random.randrange(-1, 2, 1)
    final = ruido*fator
    sensor = Sensor()
    sensor.nome='quarto'
    sensor.temperatura_quarto = 38 + final
    print(sensor.nome)
    print(sensor.temperatura_quarto)
    s.sendall(sensor.SerializeToString())
    #print('mensagem enviada')
    time.sleep(8)
    
s.close()