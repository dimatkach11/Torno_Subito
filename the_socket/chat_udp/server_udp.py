# https://www.youtube.com/watch?v=MPjgHxK8k68
import socket
import time

#print(socket.gethostname())
host = socket.gethostbyname(socket.gethostname()) # --> 192.168.1.130 --> # ! ip del serever
port = 15000    # ! porta del server

clients = [] # terrà conto degli indirizzi dei clienti collegati al server

# todo da finire