from client import Client
from cli_stub import Stub
import sys
from time import time
def main():
    inicial = time()
    stub = Stub('localhost', 8090)
    cliente = Client(stub)
    cliente.conectar()
    archivo=sys.argv[1]
    salida= sys.argv[2]
    #import pdb; pdb.set_trace()
    #respuesta = cliente.listar_archivos('.')
    #print(respuesta)
    #print(archivo)
    cliente.leer_archivo(archivo, salida)
    final = time()

    print('Tiempo: ', (final- inicial))
if __name__ == '__main__':
    main()