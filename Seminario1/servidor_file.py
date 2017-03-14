import socket

MAX_CLIENTS = 10
sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM)
sock.bind((socket.gethostname() , 13000))
sock.listen( MAX_CLIENTS )
coding = " utf−8 "

while ( True ) :
    (client , address) = sock.accept()
    name = client.recv(4000)
    msg = " Hello ,  " + name.decode( coding )
    client.sendall( bytes ( msg , encoding = coding ) )
