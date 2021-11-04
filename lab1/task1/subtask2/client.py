import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 6000

socket_client.connect((host, port))

message = input("Please enter message from client: ")
socket_client.send(message.encode('utf-8'))
server_message = socket_client.recv(1024)
print('Message received from server: ' + server_message.decode('utf-8'))
socket_client.close()
