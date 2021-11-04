import socket
from datetime import datetime
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 6000

server_socket.bind((host, port))
server_socket.listen(5)
print('The server is ready to receive connections...')

client_socket, addr = server_socket.accept()
client_message = client_socket.recv(1024).decode('utf-8')
print('Client message:', client_message, "Time when the massage was received:", str(datetime.now()))
time.sleep(5)
size_resv_bytes = client_socket.send(client_message.encode('utf-8'))
if size_resv_bytes == len(client_message):
    print("All data sent successfully!")
else:
    print("Error!")
server_socket.close()
