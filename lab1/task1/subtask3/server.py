import socket
from datetime import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 6000

server_socket.bind((host, port))
server_socket.listen(5)
print('The server is ready to receive connections...')
client_socket, addr = server_socket.accept()
while True:
    client_message = client_socket.recv(1024)
    if client_message.decode('utf-8') == 'shut up!':
        server_socket.close()
        break
    print('Client message:' + client_message.decode('utf-8') +
          "\nTime to receive the message:" + str(datetime.now()))
