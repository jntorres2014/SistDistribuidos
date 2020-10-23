import os
import pickle

class FS:
    file_manager = {}

    def list_files(path):
        try:
            return os.listdir(path)
        except Exception as e:
            print('ERROR!!! ', e)
            return None

    def open_file(path):
        #print('Abriendo...')
        try:
            if path not in FS.file_manager:
                _file = open(path, 'rb')
                FS.file_manager[path] = _file
                #print('imprimo', FS.file_manager)
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False    

    def close_file(path):
        try:
            if path in FS.file_manager:
                FS.file_manager[path].close()
                del FS.file_manager[path]
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False

    def read_file(path):
        archivo = path['value']
        offset = path['offset']
        cant_bytes = path['number_bytes']
        try:
            if FS.open_file(archivo):
                _fd = FS.file_manager[archivo]
                _fd.seek(offset)
                data = _fd.read(cant_bytes)
            FS.close_file(archivo)
            return data
        except Exception as e:
            print('error! FS read_file -> ', e)
            return None
