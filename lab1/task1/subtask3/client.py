import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 6000

socket_client.connect((host, port))
while True:
    message = input("Enter message from client: ")
    socket_client.send(message.encode('utf-8'))
    if message == 'shut up!':
        socket_client.close()
        break
