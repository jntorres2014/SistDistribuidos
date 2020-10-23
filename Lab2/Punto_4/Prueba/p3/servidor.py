from file_system import FS
from server import Server
from serv_stub import Stub

def main():
    stub = Stub(FS, 8090)
    servidor = Server(stub)
    servidor.inicializar()

if __name__ == '__main__':
    main()