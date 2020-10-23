import os
import pickle

class FS:
    def __init__(self):
        self.file_manager = {}

    def list_files(self,path):
        try:
            return os.listdir(path)
        except Exception as e:
            print('ERROR!!! ', e)
            return None

    def open_file(self,path):
        #print('Abriendo...')
        try:
            if path not in self.file_manager:
                _file = open(path, 'rb')
                self.file_manager[path] = _file
                #print('imprimo', self.file_manager)
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False    

    def close_file(self,path):
        try:
            if path in self.file_manager:
                self.file_manager[path].close()
                del self.file_manager[path]
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False

    def read_file(self,path):
        archivo = path['value']
        offset = path['offset']
        cant_bytes = path['number_bytes']
        try:
            if self.open_file(archivo):
                _fd = self.file_manager[archivo]
                _fd.seek(offset)
                data = _fd.read(cant_bytes)
            self.close_file(archivo)
            return data
        except Exception as e:
            print('error! FS read_file -> ', e)
            return None
