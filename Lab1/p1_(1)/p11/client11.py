import socket

server_address = ('0.0.0.0', 8080)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)

#message = 'I am CLIENT\n'
#client.send(message.encode('utf-8'))
while True:
    respuesta = input('Ingrese una S para salir\n')
    client.send(respuesta.encode('utf-8'))       
    from_server = client.recv(4096)
    if from_server.decode() == 's': 
        #client.close
        break

client.close()
print('cliente fin')
print(from_server.decode())