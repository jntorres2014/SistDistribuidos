import ntplib
from time import sleep
import threading
import pdb
from datetime import datetime
from tkinter import *
host1= 'ar.pool.ntp.org'
host2= 'jp.pool.ntp.org'
host3= 'europe.pool.ntp.org'
arreglo=[('fecha y hora','Offset','Delay')]

def main():
    cont=0
    c = ntplib.NTPClient()
    request = int(input('Ingrese cantidad de muestras: '))
    retardo= int(input('Delay: '))
    host= int(input('servidor: 1 argentina, 2 japon, 3 europe'))
    if host==1:
        host= host1
    elif host == 2:
        host= host2
    else: 
        host= host3
    while cont < request:
        response = c.request(host, version=3)
        sleep(retardo)
        offset=datetime.fromtimestamp(response.offset).strftime("%M:%S.%f")
        delay= datetime.fromtimestamp(response.delay).strftime("%M:%S.%f")
        hora= datetime.fromtimestamp(response.tx_time).strftime("%Y %m %d %H:%M:%-S.%f")
        arreglo.append((hora,offset,delay))
        cont = cont +1
        print("Esperando...")
    return arreglo

class Table: 
      
    def __init__(self,root,arreglo): 
        # code for creating table
        for i in range(len(arreglo)): 
            for j in range(len(arreglo[0])):
                self.e = Entry(root, width=30, fg='black',font=('Arial',12,'bold'))  
                self.e.grid(row=i, column=j) 
                self.e.insert(END, arreglo[i][j]) 
    
    def tabla():
        arreglo= main()
        total_rows = len(arreglo)        
        root = Tk()
        root.title("muestra") 
        t = Table(root,arreglo) 
        root.mainloop() 

Table.tabla()
