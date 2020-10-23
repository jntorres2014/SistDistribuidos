import grpc
import pdb
from file_system_pb2 import Path, PathRead
from file_system_pb2_grpc import FSStub

file_manager = {}
class Stub:

    def __init__(self, host='0.0.0.0', port='50051'):
        self._appliance = ':'.join([host, port])
        self._channel = None
        self._stup = None

    def connect(self):
        """ Returns a gRPC open channel """
        try:
            self._channel = grpc.insecure_channel(self._appliance)
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
            path = Path(value = path)
            response = self._stub.ListFiles(path)          
            print (response)
            return response.values
        return None
    
    def read_file2(self, path):
        if self.is_connected():    
            path = Path(value = path)
            print('paso')
            fileData = self._stub.Read(path)
            return fileData.data
        return None

    def read_file(self, path, offset, number_bytes):
        if self.is_connected():
            #Armo mi paquete PathRead que me pide gRPC
            path = PathRead(value=path, offset=offset, number_bytes=number_bytes)
            response = self._stub.Read(path)
            return response.data
        else:
            return None

