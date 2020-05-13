import socket

# TCP client
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 5001
print("host : ", host, " port : ", port)

clientsocket.connect((host,port))

message = clientsocket.recv(1024)

print(message.decode())

clientsocket.close()


