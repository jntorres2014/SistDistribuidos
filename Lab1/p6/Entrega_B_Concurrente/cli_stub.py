import socket
import pickle
import pdb
from structures import (
    Path, 
    PathFiles,
    PathRead,
)
cant_buff = 1024

class FSStub():

    def __init__(self, canal):
        self._channel = canal
    
    def ListFiles(self, path):
        self._channel.sendall(path)
        lista= self._channel.recv(cant_buff)
        return lista        

    def Read(self,path):
        self._channel.sendall(path)
        request = self._channel.recv(cant_buff)
        return request


class Stub:

    def __init__(self, host='0.0.0.0', port='8090'):
        self._appliance = (host, port)
        print(host,port)
        self._channel = None
        self._stub = None

    def connect(self):
        """ Returns a Socket channel """
        try:
            self._channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._channel.connect(self._appliance)
            self._stub = FSStub(self._channel)
            print('Cliente Conectado!!..')
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
            request= self._stub.ListFiles(path)
            return request
        return None

    def read_file(self, path):
        if self.is_connected():
            return self._stub.Read(path)
        return None

