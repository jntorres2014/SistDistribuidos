from client import Client
from cliente_stub import Stub
import pdb
import sys

def main():
    stub = Stub('localhost', '50051')
    cliente = Client(stub)
    cliente.conectar()
    archivo=sys.argv[1]
    print(archivo)
    salida= sys.argv[2]
    #Texto
    #cliente.leer_archivo(archivo, salida)
    #PDF
    cliente.leer_archivo(archivo, salida)
    #Video
    #cliente.leer_archivo(archivo, salida)
    #pdb.set_trace()
    print('Lectura completa.')

if __name__ == '__main__':
    main()
