import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 6000

socket_client.connect((host, port))
message = input("Enter client message: ")
socket_client.send(message.encode('utf-8'))
socket_client.close()
