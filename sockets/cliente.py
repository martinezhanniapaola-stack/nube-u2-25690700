import socket
c = socket.socket()
c.connect(("localhost", 5002))
c.send(b"Hola")
print(c.recv(1024))
