import socket
import pendulum
import tools

def final_clock(clocks): # implementar, mirar algoritmo.
    current = pendulum.now("Europe/Madrid")
    print(current.to_time_string())
    min = ((current.minute-clocks[0].minute) + (current.minute-clocks[1].minute))/3
    sec = ((current.second-clocks[0].second) + (current.second-clocks[1].second))/3
    current = current.add(minutes=min)
    current = current.add(seconds=sec)
    return current


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_response = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("localhost", tools.PORT))
MAX_CLIENT = 2
BUFFER_SIZE=1000
received = []
clocks = []


for i in range(MAX_CLIENT):
    data, address = sock.recvfrom(BUFFER_SIZE)
    its_clock = pendulum.parse(data.decode("utf-8"))
    print("Received " +its_clock.to_time_string() +" from : " +str(address))
    clocks.append(its_clock)
    received.append(address)
    sock_response.sendto(b"Recibido", address)
   
# Decido lo que hacer
final_clock = final_clock(clocks)
print("Final clock: {}".format(final_clock))

# Lo envio a los clientes esperando
sock_response.sendto(tools.clock_to_bytes(final_clock),received[0])
sock_response.sendto(tools.clock_to_bytes(final_clock),received[1])
sock_response.close()
