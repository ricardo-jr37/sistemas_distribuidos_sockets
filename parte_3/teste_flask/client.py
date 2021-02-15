from flask import Flask, url_for
from flask import render_template
from flask import request
import socket
import pdb
from sensores_pb2 import Sensor
import time
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    ligada = request.form.get('lampada-ligada')
    tmp = request.form.get('ar')
    print(ligada)
    print(tmp)
    server_lampada(ligada)
    server_ar(tmp)
    return render_template('index.html')

def server_lampada(ligada):
    teste = Sensor()
    teste.nome = 'lampada'
    teste.status_lampada = int(ligada)
    PORT = 1510
    HOST = 'localhost'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(teste.SerializeToString())
    s.close()

def server_ar(temperatura):
    teste = Sensor()
    #pdb.set_trace()
    teste.nome = 'cozinha'
    teste.temperatura_cozinha = float(temperatura)
    PORT = 1510
    HOST = 'localhost'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(teste.SerializeToString())
    s.close()
'''
def server_ar(temperatura):
	teste = Sensor()
	teste.nome = 'cozinha'
	teste.temperatura_cozinha = int(temperatura)
    PORT = (1510)
    HOST = 'localhost'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(teste.SerializeToString())
    s.close()
'''

if __name__ == '__main__':
    app.run(port=8080, debug=True)