import sockets

from structures import (
    Path, 
    PathFiles,
    PathRead,
)


class FSStub:

    def __init__(self, canal):
        self._channel = canal

    def ListFiles(self, path):
        path = Path(path=path, operacion=1)
        self._channel.sendall(path)
        path_files = PathFiles()
        list_files = []
        while self._channel.recv_into(path_files):
            list_files.append(path_files.values)

        return list_files

    def Read (self,path):
        path = PathFiles(value=path,operacion=2,path=path,offset=,number_bytes=)
        self._channel.sendall(path)
        datos= self._channel.recv(4096)
        request= 
        #self._channel.
        return path

class Stub:

    def __init__(self, host='0.0.0.0', port='8090'):
        self._appliance = (host, port)
        self._channel = None
        self._stup = None

    def connect(self):
        """ Returns a gRPC open channel """
        try:
            self._channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._channel.connect(self._appliance)
            self._stub = FSStub(self._channel)
            return True if self._channel else False
        except Exception as e:
            print('Error when openning channel {}'.format(e))
            return False

    def disconnect(self):
        self._channel.close()
        self._channel = None

    def is_connected(self):
        return self._channel

    def list_files(self, path):
        if self.is_connected():
            return self._stub.ListFiles(path)
        return None
    
    def read_file(self, path, offset, number_bytes):
        if self.is_connected():
        paquete = file_system_structures.PathRead()
        paquete.value = path
        paquete.offset = offset
        paquete.number_bytes = number_bytes
        paquete.operacion = 2
        #armo el paquete para mandar al Read
        response = self._stub.Read(paquete)
        return response
        else:
        return None
