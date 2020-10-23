import socket

server_address = (('0.0.0.0', 8080))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen()

message = 'Tu conexion fue cerrada con Exito!!\n'

while True:
	print('Server disponible!')
	connection, client_address = server.accept()
	from_client = ''
	while True:
		data = connection.recv(4096)
		#connection.send(data.encode('utf-8'))
		if data.decode() == 's':break
		from_client += data.decode() #acumula los mensajes que llegan.
		connection.send(from_client.encode('utf-8'))
	print('salio')	
	connection.send(data)
	connection.close()
	print('cliente desconectado \n')

