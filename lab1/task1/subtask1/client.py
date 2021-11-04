import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 6000))

message = input("Please enter message from client: ")
client_socket.sendall(message.encode('utf-8'))
client_socket.close()
