
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(),13000))
sock.sendall(b"Juan")
max_size = 1000
msg = sock.recv(max_size)
print(msg)
