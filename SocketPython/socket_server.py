import socket

# create the server socket with python3
# AF_INET --> Internet Protocol v4 addresses
# TCP almost always uses SOCK_STREAM and UDP uses SOCK_DGRAM
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# you can aslo specify the host manually 
host = socket.gethostname()
port = 5001
print("current host :", str(host), " port : ", port)

# binding the socket
serversocket.bind(('192.168.43.73', port))

# tcp listener - here 3 maximum connection
serversocket.listen(3)

while True:

    # starting connection 
    clientsocket, address = serversocket.accept()
    print("received connnection from %s" % str(address))
    message = 'hello! you are connected to the server !'

    # encode is necessary for python3 but not python2
    clientsocket.send(message.encode())
    clientsocket.close()





