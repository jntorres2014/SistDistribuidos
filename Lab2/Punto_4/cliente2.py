import socket
import time

server_address = ('0.0.0.0', 8080)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)

#message = 'I am CLIENT\n'
#client.send(message.encode('utf-8'))
respuesta = input('pedir hora S\n')
while True:
    client.send(respuesta.encode('utf-8'))       
    if input('desea pedir otra hora ? ') == 's':
        client.close
        break
    from_server = client.recv(4096)
    print(from_server)
time.sleep(4)
#client.close()
print('cliente fin')
print(from_server.decode())