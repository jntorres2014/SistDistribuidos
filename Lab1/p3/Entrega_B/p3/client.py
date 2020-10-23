import pickle
class Client:

    def __init__(self, adapter):
        self.adapter = adapter

    def conectar(self):
        try:
            self.adapter.connect()
        except Exception as e:
            print('Connection error {e}')

    def desconectar(self):
        self.adapter.disconnect()

    def esta_conectado(self):
        return self.adapter.is_connected()

    def listar_archivos(self, path):
        paquete = { 'value': path, 'operacion': 1}
        objeto_a_enviar = pickle.dumps(paquete)
        request = self.adapter.list_files(objeto_a_enviar)
        requestList = []
        requestPickle=pickle.loads(request)
        for i in requestPickle['value']:
            requestList.append(i)
        return requestList


    def read_file(self, path,offset,number_bytes):
        paquete = { 'value': path, 'offset': offset, 'number_bytes': number_bytes, 'operacion':2}
        objeto_a_enviar = pickle.dumps(paquete) 
        request=self.adapter.read_file(objeto_a_enviar)
        requestPickle = pickle.loads(request)
        return requestPickle['value']
        

    def leer_archivo(self, path,salida):
        offset = 0
        number_bytes = 512
        Leyendo = True
        try:
            with open(salida, 'wb') as archivo:
                while Leyendo:
                    data = self.read_file(path, offset, number_bytes)
                    offset = offset + len(data)
                    if not (offset%number_bytes==0) :
                        Leyendo = False
                    archivo.write(data)
                    print('offset', round(offset/(1024*1024),2),'MB')
        except Exception as e:
            print('ERROR -> -client- read file ', e)
            return 0
