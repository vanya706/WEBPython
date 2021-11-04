import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 6000

server_socket.bind((host, port))
server_socket.listen(5)
print('The server is ready to receive connections...')
while True:
    client_socket, addr = server_socket.accept()
    client_message = client_socket.recv(1024)
    if client_message.decode('utf-8') == 'stop':
        server_socket.close()
        break
    print('Client message:' + client_message.decode('utf-8'))
server_socket.close()
