from file_system import FS
from server import Server
from server_stub import Stub 
import pdb

def main():
    stub = Stub(FS, '50051')
    servidor = Server(stub)
    #pdb.set_trace()
    servidor.inicializar()
    #pdb.set_trace()
if __name__ == '__main__':
    main()
