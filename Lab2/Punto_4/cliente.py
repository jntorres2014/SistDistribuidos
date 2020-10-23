import ntplib
from time import sleep
import threading
import pdb
from datetime import datetime
from tkinter import *
host2= 'europe.pool.ntp.org'
host = 'pool.ntp.org'


#def tablas(respose):
    
def main():
    c = ntplib.NTPClient()
    #r4.set(host2)
    cont=0
    media=0
    menor_rtt=0

    while cont <10:
        sleep(1)
        response = c.request(host, version=3)
        hora_mia1= datetime.now()
        hora= datetime.utcfromtimestamp(response.tx_time)
        hora_mia2= datetime.now()
        #.strftime("%H:%M:%-S") 
        rtt= (hora_mia2 - hora_mia1)/2 
        print(rtt)
        hora_server_rtt=  hora + rtt
        if  menor_rtt == 0 :
            menor_rtt = hora_server_rtt
        else: 
            if hora_server_rtt < menor_rtt:
                menor_rtt = hora_server_rtt
        print('menor rtt',menor_rtt)
        cont= cont+1
 
main()    

'''
# Configuración de la raíz
root = Tk()
root.config(bd=20)
r = StringVar()
r2 = StringVar()
r3 = StringVar()
r4 = StringVar()
Label(root, text="Host Hora").pack()
Entry(root, justify="center", textvariable=r4).pack()

Label(root, text="Version").pack()
Entry(root, justify="center", textvariable=r3).pack()

Label(root, text="Hora ").pack()
Entry(root, justify="center", textvariable=r).pack()

Label(root, text="Ofsset").pack()
Entry(root, justify="center", textvariable=r2 ).pack()


Button(root, text="Pedir hora", command=main).pack(side="right")

root2 = Tk()

height = 2
width = 2
for i in range(height): #Rows
       #Entry(root, justify="center", textvariable=r2 ).pack()
       for j in range(width): #Columns
           b = Entry(root2, text="hola")
           b.grid(row=i, column=j,textvariable= r2)
           Entry(root, justify="center", textvariable=r2 ).pack()


# Finalmente bucle de la aplicación
root.mainloop()
'''