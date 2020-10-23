
class Client:
    def __init__ (self, adapter=None):
        self.adapter = adapter

    def conectar(self):
        self.adapter.connect()

    def desconectar(self):
        #self.adapter.desconectar()
        self.adapter.disconnect()

    def enviar(self,mensaje):
        self.adapter.enviar(mensaje)

    def recibir(self):
        return self.adapter.recibir()
    
    #FALTA?
    def listar_archivos(self,path):
        return self.adapter.list_files(path)


    def abrir_archivo(self,path):
        return self.adapter.open_file(path)

    def cerrar_archivo(self,path):
        return self.adapter.close_file(path)

    def leer_archivo(self, path, salida):
        offset = 0
        number_bytes = 4096
        Leyendo = True
        try:
            with open(salida, 'wb') as archivo:
                while Leyendo:
                    data = self.adapter.read_file(path, offset, number_bytes)
                    offset = offset + len(data)
                    if not (offset%number_bytes==0) :
                        Leyendo = False
                    archivo.write(data)
                    print('offset', round(offset/(1024*1024),2),'MB')
        except Exception as e:
            print('ERROR -> -client- read file ', e)
                
            return 0
