import socket
import pickle 
import pdb
import threading
cant_buff = 1024

class FSStub(threading.Thread):

    def __init__(self, canal, file_system_adapter, client):
        self._channel = canal
        self._adapter = file_system_adapter
        self._client = client
        threading.Thread.__init__(self) 
        
        #self.stoprequest = threading.Event()
        #threading.self._process_request()
        #self._process_request()

  
    def run(self):

        while True:
            data = self._channel.recv(cant_buff)
            if data:
                dataPickle = pickle.loads(data)
                #pdb.set_trace()
                if dataPickle is not None:
                    if dataPickle['operacion'] == 1:
                        path_files = self._adapter.list_files(dataPickle['value'])
                        request = { 'value': path_files}
                        requestPickle= pickle.dumps(request)
                        self._channel.send(requestPickle)
                        #pdb.set_trace()
                        #return 0
                    elif dataPickle['operacion'] == 2:
                        read_file = self._adapter.read_file(dataPickle)
                        request = { 'value': read_file}
                        requestPickle= pickle.dumps(request)
                        self._channel.sendall(requestPickle)
                    #return 0
            else:
                break


class Stub:

    def __init__(self, adapter, port='8090'):
        self._port = port
        self._adapter = adapter
        self.server = None
        self._stub = None
    

    def _setup(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', 8090))     
    
    def run(self):
        self._setup()
        self.server.listen()
        try:    
            
            while True:
                connection, client_address = self.server.accept()
                print('cliente',client_address)
                print('conectando')
                self._stub = FSStub(connection, self._adapter(),client_address)
                self._stub.start()
        except KeyboardInterrupt:
            connection.close()
            self.server.stop()
