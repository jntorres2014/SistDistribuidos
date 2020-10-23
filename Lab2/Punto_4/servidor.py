import socket
from datetime import datetime
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
		now= datetime.now()
		response= now.strftime('%m/%d/%Y')
		connection.send(response.encode('utf-8'))
	print('salio')	
	#connection.send(data)
	connection.close()
	print('cliente desconectado \n')

